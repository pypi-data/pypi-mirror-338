How to import pyrinox's library is as follows:

<< from pyrinox import rubino>>

An example:

		
from pyrinox import rubino
import asyncio
async def main():
    async with rubino("auth") as bot:
        1
        data = await bot.search_username("@rubika")
        print(data)
asyncio.run(main())


