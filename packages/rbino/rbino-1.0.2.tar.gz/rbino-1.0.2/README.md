from rbino import rubino
import asyncio

async def main():
    async with rubino("YOUR_AUTH") as bot:
        # Follow a user by their ID
        follow_result = await bot.follow("USER_ID")
        print("Follow Status:", follow_result)

asyncio.run(main())