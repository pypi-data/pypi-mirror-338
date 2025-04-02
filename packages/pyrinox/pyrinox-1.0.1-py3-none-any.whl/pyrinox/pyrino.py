from aiohttp import ClientSession
import asyncio
import random
import json
import aiofiles
import aiohttp
from pathlib import Path
from tqdm import tqdm
import time
from typing import Optional, List, Dict, Union, Any
import logging


class Rubino:
    """
    An enhanced Rubino API client with improved performance and error handling.
    
    Features:
    - Colorful console output
    - Better error handling
    - Performance optimizations
    - Type hints
    - Async context manager
    - Progress bars for uploads
    - Connection pooling
    - Retry mechanism
    """
    
    def __init__(self, auth: str):
        """
        Initialize Rubino client with authentication token.
        
        Args:
            auth: Your Rubino authentication token
        """
        self.auth = auth
        self.session: Optional[ClientSession] = None
        self._print_banner()
        self.logger = self._setup_logger()
        
    def _print_banner(self):
        """Print a colorful banner with creator info."""
        banner = r"""
  █▀▀█ █░░█ █▀▀█ ░▀░ █▀▀▄ █▀▀█
█░░█ █▄▄█ █▄▄▀ ▀█▀ █░░█ █░░█
█▀▀▀ ▄▄▄█ ▀░▀▀ ▀▀▀ ▀░░▀ ▀▀▀▀
                                  
 @MrAminEbrahimi 
"""
        colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
        colored_banner = ""
        for i, line in enumerate(banner.split('\n')):
            colored_banner += colors[i % len(colors)] + line + '\033[0m\n'
        print(colored_banner)
        
    def _setup_logger(self):
        """Configure logger for the class."""
        logger = logging.getLogger('Rubino')
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(
            '\033[92m%(asctime)s - %(name)s - %(levelname)s\033[0m - %(message)s'
        ))
        logger.addHandler(handler)
        return logger
        
    async def __aenter__(self):
        """Async context manager entry."""
        self.logger.info("Initializing session...")
        self.session = ClientSession(
            connector=aiohttp.TCPConnector(limit=30, force_close=True),
            timeout=aiohttp.ClientTimeout(total=60),
            trust_env=True
        )
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        if self.session:
            self.logger.info("Closing session...")
            await self.session.close()
            self.session = None
        return None
        
    async def _retry_request(self, method: str, url: str, max_retries: int = 3, **kwargs) -> Any:
        """
        Retry mechanism for requests.
        
        Args:
            method: HTTP method ('GET' or 'POST')
            url: Target URL
            max_retries: Maximum number of retries
            **kwargs: Additional arguments for the request
            
        Returns:
            Response data
            
        Raises:
            Exception: If all retries fail
        """
        last_exception = None
        for attempt in range(max_retries):
            try:
                if method == 'GET':
                    async with self.session.get(url, **kwargs) as res:
                        return await res.text()
                else:
                    async with self.session.post(url, **kwargs) as res:
                        return await res.json()
            except Exception as e:
                last_exception = e
                wait_time = min(2 ** attempt, 5)  # Exponential backoff with max 5 seconds
                self.logger.warning(f"Attempt {attempt + 1} failed, retrying in {wait_time}s...")
                await asyncio.sleep(wait_time)
                
        raise Exception(f"Request failed after {max_retries} attempts") from last_exception
        
    async def GET(self, url: str) -> str:
        """
        Perform a GET request.
        
        Args:
            url: Target URL
            
        Returns:
            Response text
            
        Raises:
            RuntimeError: If session is not initialized
        """
        if not self.session:
            raise RuntimeError("Session is not initialized")
            
        self.logger.debug(f"GET request to {url}")
        return await self._retry_request('GET', url)
        
    async def POST_DATA(self, method: str, input: Dict, auth: Optional[str] = None) -> Dict:
        """
        Perform a POST request to Rubino API.
        
        Args:
            method: API method name
            input: Input data for the API
            auth: Optional auth token (defaults to instance auth)
            
        Returns:
            API response as dictionary
        """
        url = f"https://rubino{random.randint(1,30)}.iranlms.ir/"
        
        payload = {
            "api_version": "0",
            "auth": self.auth if not auth else auth,
            "client": {
                "app_name": "Main",
                "app_version": "3.5.7",
                "lang_code": "fa",
                "package": "app.rbmain.a",
                "temp_code": "31",
                "platform": "Android"
            },
            "data": input,
            "method": method
        }
        
        self.logger.debug(f"POST request to {url} with method {method}")
        start_time = time.time()
        
        try:
            response = await self._retry_request(
                'POST',
                url,
                json=payload,
                headers={'Content-Type': 'application/json'}
            )
            
            elapsed = time.time() - start_time
            self.logger.info(f"API call '{method}' completed in {elapsed:.2f}s")
            
            return response
        except Exception as e:
            self.logger.error(f"API call '{method}' failed: {str(e)}")
            raise
            
    async def get_me(self, profile_id: Optional[str] = None) -> Dict:
        """Get current user profile info."""
        return await self.POST_DATA("getMyProfileInfo", {"profile_id": profile_id})
        
    async def follow(self, follow_id: str, profile_id: Optional[str] = None) -> str:
        """Follow a user."""
        return await self.POST_DATA('requestFollow', {
            "f_type": "Follow",
            "followee_id": follow_id,
            "profile_id": profile_id
        })
        
    async def upload_chunk(self, url: str, data: bytes, headers: Dict) -> Dict:
        """Upload a file chunk."""
        async with self.session.post(url, data=data, headers=headers) as res:
            return await res.json()
            
    async def fetch_file_content(self, url: str) -> bytes:
        """Fetch file content from URL."""
        async with self.session.get(url) as response:
            if response.status == 200:
                return await response.read()
            raise Exception(f"Failed to fetch file: {response.status}")
            
    async def upload_file(
        self,
        file: Union[str, Path],
        file_type: str = "Picture",
        profile_id: Optional[str] = None,
        file_name: Optional[str] = None
    ) -> List:
        """
        Upload a file to Rubino.
        
        Args:
            file: File path or URL
            file_type: Type of file ('Picture' or 'Video')
            profile_id: Target profile ID
            file_name: Custom file name
            
        Returns:
            List containing file info and hash
        """
        # Determine if file is local or remote
        file_path = Path(file)
        if not file_path.exists():
            self.logger.info(f"Downloading file from {file}...")
            bytef = await self.fetch_file_content(file)
            file_name = file_name or f"rubino_{file_type.lower()}.{'jpg' if file_type == 'Picture' else 'mp4'}"
        else:
            self.logger.info(f"Reading local file {file_path}...")
            async with aiofiles.open(file_path, 'rb') as f:
                bytef = await f.read()
        
        # Prepare upload request
        request_data = {
            "file_name": file_name or file_path.name,
            "file_size": len(bytef),
            "file_type": file_type,
            "profile_id": profile_id
        }
        
        # Request upload
        response = await self.POST_DATA("requestUploadFile", request_data)
        file_id = response["data"]["file_id"]
        hash_send = response["data"]["hash_file_request"]
        url = response["data"]["server_url"]
        
        # Prepare headers
        headers = {
            'auth': self.auth,
            'Host': url.replace("https://", "").replace("/UploadFile.ashx", ""),
            'chunk-size': str(len(bytef)),
            'file-id': str(file_id),
            'hash-file-request': hash_send,
            "content-type": "application/octet-stream",
            "accept-encoding": "gzip",
            "user-agent": "okhttp/3.12.1"
        }
        
        # Upload in chunks with progress bar
        chunk_size = 131072  # 128KB chunks
        chunks = [bytef[i:i + chunk_size] for i in range(0, len(bytef), chunk_size)]
        
        with tqdm(
            total=len(bytef),
            unit='B',
            unit_scale=True,
            desc=f"Uploading {file_type}",
            bar_format='{l_bar}{bar:30}{r_bar}{bar:-10b}',
            colour='green'
        ) as pbar:
            for i, chunk in enumerate(chunks, start=1):
                headers['chunk-size'] = str(len(chunk))
                headers['part-number'] = str(i)
                headers['total-part'] = str(len(chunks))
                
                results = await self.upload_chunk(url, chunk, headers)
                pbar.update(len(chunk))
                
        return [response["data"], results['data']['hash_file_receive']]
        
    async def add_post(
        self,
        file: Union[str, Path],
        text: Optional[str] = None,
        post_type: str = "Picture",
        profile_id: Optional[str] = None,
        thumbnail: Optional[str] = None,
        file_name: Optional[str] = None
    ) -> Dict:
        """
        Add a new post.
        
        Args:
            file: File path or URL
            text: Caption text
            post_type: Type of post ('Picture' or 'Video')
            profile_id: Target profile ID
            thumbnail: Thumbnail URL (for videos)
            file_name: Custom file name
            
        Returns:
            API response
        """
        data = await self.upload_file(file, file_type=post_type, file_name=file_name, profile_id=profile_id)
        
        if post_type == "Picture":
            input = {
                "caption": text,
                "file_id": data[0]["file_id"],
                "hash_file_receive": data[1],
                "height": 800,
                "width": 800,
                "is_multi_file": False,
                "post_type": "Picture",
                "rnd": random.randint(100000, 999999999),
                "thumbnail_file_id": data[0]["file_id"],
                "thumbnail_hash_file_receive": data[1],
                "profile_id": profile_id
            }
        elif post_type == "Video":
            thumb = await self.upload_file(
                thumbnail or "https://cdn.imgurl.ir/uploads/g70585_IMG_20250401_112003_518.jpg",
                file_type="Picture",
                file_name="thumbnail.jpg",
                profile_id=profile_id
            )
            input = {
                "caption": text,
                "duration": "8",
                "file_id": data[0]["file_id"],
                "hash_file_receive": data[1],
                "height": "1410",
                "is_multi_file": None,
                "post_type": "Video",
                "rnd": random.randint(100000, 999999999),
                "snapshot_file_id": thumb[0]["file_id"],
                "snapshot_hash_file_receive": thumb[1],
                "tagged_profiles": [],
                "thumbnail_file_id": thumb[0]["file_id"],
                "thumbnail_hash_file_receive": thumb[1],
                "width": "1080",
                "profile_id": profile_id
            }
            
        return await self.POST_DATA("addPost", input)
        
    # All other methods remain the same as in your original code, but with:
    # 1. Type hints added
    # 2. Better error handling
    # 3. Logging
    # 4. Docstrings
    
    async def get_post_by_share_link(self, link: str, profile_id: Optional[str] = None) -> Dict:
        """Get post by share link."""
        if link.startswith("https://rubika.ir/post/"):
            link = link.split()[0][23:]
        return await self.POST_DATA("getPostByShareLink", {"share_string": link, "profile_id": profile_id})
        
    async def add_post_view_count(self, post_id: str, target_post_id: str, profile_id: Optional[str] = None) -> str:
        """Add view count to a post."""
        return await self.POST_DATA("addPostViewCount", {
            "post_id": post_id,
            "post_profile_id": target_post_id,
            "profile_id": profile_id
        })
        
    async def delete_post(self, post_id: str, profile_id: Optional[str] = None) -> Dict:
        """Delete a post."""
        return await self.POST_DATA("removeRecord", {
            "model": "Post",
            "profile_id": profile_id,
            "record_id": post_id
        })
        
    async def get_explore_posts(
        self,
        limit: int = 21,
        sort: str = "FromMax",
        max_id: Optional[str] = None,
        profile_id: Optional[str] = None
    ) -> Dict:
        """Get explore posts."""
        return await self.POST_DATA("getExplorePosts", {
            "profile_id": profile_id,
            "limit": limit,
            "sort": sort,
            "max_id": max_id
        })
        
    async def search_profile(
        self,
        username: str,
        limit: int = 20,
        profile_id: Optional[str] = None
    ) -> Dict:
        """Search for profiles."""
        return await self.POST_DATA("searchProfile", {
            "username": username,
            "limit": limit,
            "profile_id": profile_id
        })
        
    async def edit_profile(self, **kwargs) -> Dict:
        """Edit profile information."""
        if "bio" in kwargs:
            return await self.POST_DATA("updateProfile", {
                "bio": kwargs.get("bio"),
                "profile_id": kwargs.get("profile_id"),
                "profile_status": "Public"
            })
        elif "image" in kwargs:
            data = await self.upload_file(
                file=kwargs.get("image"),
                file_type="Picture",
                file_name=kwargs.get("file_name"),
                profile_id=kwargs.get("profile_id")
            )
            
            if "thumbnail" in kwargs:
                thumb = await self.upload_file(
                    kwargs.get("image"),
                    file_type="Picture",
                    file_name=kwargs.get("file_name"),
                    profile_id=kwargs.get("profile_id")
                )
                input = {
                    "file_id": data[0]["file_id"],
                    "hash_file_receive": data[1],
                    "thumbnail_file_id": thumb[0]["file_id"],
                    "thumbnail_hash_file_receive": thumb[1],
                    "profile_id": kwargs.get("profile_id")
                }
            else:
                input = {
                    "file_id": data[0]["file_id"],
                    "hash_file_receive": data[1],
                    "thumbnail_file_id": data[0]["file_id"],
                    "thumbnail_hash_file_receive": data[1],
                    "profile_id": kwargs.get("profile_id")
                }
            return await self.POST_DATA("updateProfilePhoto", input)
            
    async def search_hash_tag(
        self,
        content: str,
        limit: int = 20,
        profile_id: Optional[str] = None
    ) -> Dict:
        """Search by hashtag."""
        return await self.POST_DATA("searchHashTag", {
            "content": content,
            "limit": limit,
            "profile_id": profile_id
        })
        
    async def un_follow(self, user_id: str, profile_id: Optional[str] = None) -> Dict:
        """Unfollow a user."""
        return await self.POST_DATA("requestFollow", {
            "followee_id": user_id,
            "f_type": "Unfollow",
            "profile_id": profile_id
        })
        
    async def get_profile_stories(
        self,
        limit: int = 100,
        profile_id: Optional[str] = None
    ) -> Dict:
        """Get profile stories."""
        return await self.POST_DATA("getProfileStories", {
            "limit": limit,
            "profile_id": profile_id
        })
        
    async def get_story_ids(
        self,
        target_profile_id: str,
        profile_id: Optional[str] = None
    ) -> Dict:
        """Get story IDs."""
        return await self.POST_DATA("getStoryIds", {
            "profile_id": profile_id,
            "target_profile_id": target_profile_id
        })
        
    async def get_comments(
        self,
        post_id: str,
        post_profile_id: str,
        limit: int = 100,
        profile_id: Optional[str] = None,
        sort: str = "FromMax",
        equal: bool = False
    ) -> Dict:
        """Get post comments."""
        return await self.POST_DATA("getComments", {
            "equal": equal,
            "limit": limit,
            "sort": sort,
            "post_id": post_id,
            "profile_id": profile_id,
            "post_profile_id": post_profile_id
        })
        
    async def get_profile_list(
        self,
        equal: bool = False,
        limit: int = 10,
        sort: str = "FromMax"
    ) -> Dict:
        """Get profile list."""
        return await self.POST_DATA("getProfileList", {
            "equal": equal,
            "limit": limit,
            "sort": sort
        })
        
    async def get_my_profile_info(self, profile_id: Optional[str] = None) -> Dict:
        """Get current user profile info."""
        return await self.POST_DATA("getMyProfileInfo", {"profile_id": profile_id})
        
    async def like_post(
        self,
        post_id: str,
        target_post_id: str,
        profile_id: Optional[str] = None
    ) -> Dict:
        """Like a post."""
        return await self.POST_DATA("likePostAction", {
            "action_type": "Like",
            "post_id": post_id,
            "post_profile_id": target_post_id,
            "profile_id": profile_id
        })
        
    async def get_share_link(
        self,
        post_id: str,
        post_profile_id: str,
        profile_id: Optional[str] = None
    ) -> Dict:
        """Get share link for a post."""
        return await self.POST_DATA("getShareLink", {
            "post_id": post_id,
            "post_profile_id": post_profile_id,
            "profile_id": profile_id
        })
        
    async def search_username(self, username: str) -> Dict:
        """Search for username."""
        if username.startswith("@"):
            username = username.replace("@", "")
        return await self.POST_DATA("isExistUsername", {"username": username})
        
    async def add_view_story(
        self,
        story_profile_id: str,
        story_ids: List[str],
        profile_id: Optional[str] = None
    ) -> Dict:
        """Add view to stories."""
        return await self.POST_DATA("addViewStory", {
            "profile_id": profile_id,
            "story_ids": story_ids,
            "story_profile_id": story_profile_id
        })
        
    async def create_page(
        self,
        name: str,
        username: str,
        bio: Optional[str] = None
    ) -> Dict:
        """Create a new page."""
        return await self.POST_DATA("createPage", {
            "bio": bio,
            "name": name,
            "username": username
        })
        
    async def add_comment(
        self,
        text: str,
        post_id: str,
        post_profile_id: str,
        profile_id: Optional[str] = None
    ) -> Dict:
        """Add comment to a post."""
        return await self.POST_DATA("addComment", {
            "content": text,
            "post_id": post_id,
            "post_profile_id": post_profile_id,
            "rnd": f"{random.randint(0, 999999)}",
            "profile_id": profile_id
        })
        
    async def get_profile_posts(
        self,
        target_profile_id: str,
        limit: int = 1,
        profile_id: Optional[str] = None
    ) -> Dict:
        """Get profile posts."""
        return await self.POST_DATA("getProfilePosts", {
            "limit": limit,
            "sort": "FromMax",
            "target_profile_id": target_profile_id,
            "profile_id": profile_id
        })
        
    async def un_like_post(
        self,
        post_id: str,
        post_profile_id: str,
        profile_id: Optional[str] = None
    ) -> Dict:
        """Unlike a post."""
        return await self.POST_DATA("likePostAction", {
            "action_type": "Unlike",
            "post_id": post_id,
            "post_profile_id": post_profile_id,
            "profile_id": profile_id
        })
        
    async def post_book_mark_action(
        self,
        post_id: str,
        post_profile_id: str,
        profile_id: Optional[str] = None
    ) -> Dict:
        """Bookmark a post."""
        return await self.POST_DATA("postBookmarkAction", {
            "action_type": "Bookmark",
            "post_id": post_id,
            "post_profile_id": post_profile_id,
            "profile_id": profile_id
        })