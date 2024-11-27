import discord
from discord.ext import commands
import json
import logging
from cogs.sledge_cog import SledgeCog
import asyncio

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Read the bot token from the file
with open('token.txt', 'r') as file:
    TOKEN = file.read().strip()

# Configure intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

# Create bot instance
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
        logger.info(f'Logged in as {self.user} (ID: {self.user.id})')
        logger.info('------')
        
        # Sync commands
        try:
            logger.info("Starting command sync...")
            await self.tree.sync()
            logger.info("Command tree synced successfully!")
        except Exception as e:
            logger.error(f"Failed to sync commands: {e}")

bot = SledgeBot()

# Run the bot
async def main():
    async with bot:
        try:
            await bot.start(TOKEN)
        except Exception as e:
            logger.error(f"Error starting bot: {e}")

if __name__ == "__main__":
    asyncio.run(main())
