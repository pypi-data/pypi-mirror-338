How to import aminpy's library is as follows:

<< from aminpy import rubino>>

An example:

		
from aminpy import rubino
import asyncio
async def main():
    async with rubino("auth") as bot:
        
        data = await bot.search_username("@rubika")
        print(data)
asyncio.run(main())


