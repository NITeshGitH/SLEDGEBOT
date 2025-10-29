import discord
from discord.ext import commands
import logging
from cogs.sledge_cog import SledgeCog
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

class SledgeBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='/',
            intents=intents,
            application_id=1248678483316707471
        )
    
    async def setup_hook(self):
        await self.add_cog(SledgeCog(self))
        logger.info("SledgeCog has been loaded")

    async def on_ready(self):
        assert self.user is not None
        logger.info(f'Logged in as {self.user} (ID: {self.user.id})')
        logger.info('------')
      
        try:
            logger.info("Starting command sync...")
            await self.tree.sync()
            logger.info("Command tree synced successfully!")
        except Exception as e:
            logger.error(f"Failed to sync commands: {e}")

bot = SledgeBot()

async def main():
    TOKEN = os.getenv('DISCORD_TOKEN')
    if not TOKEN:
        logger.error("No token found in environment variables!")
        raise ValueError("Discord token not found")

    async with bot:
        try:
            await bot.start(TOKEN)
        except Exception as e:
            logger.error(f"Error starting bot: {e}")

if __name__ == "__main__":
    asyncio.run(main())
