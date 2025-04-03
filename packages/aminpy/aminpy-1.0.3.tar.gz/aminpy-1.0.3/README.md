from aminpy import rubino
import asyncio
from termcolor import colored
#AminEbrahimi
async def main():
    async with rubino("YOUR_AUTH_TOKEN") as bot:
        # Upload an image post
        post = await bot.add_post(
            "image.jpg",
            text="Hello from aminpy!",
            type="Picture"
        )
        print(colored("Post Created:", "green"), post)

asyncio.run(main())