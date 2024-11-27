import discord
from discord import app_commands
from discord.ext import commands
import json
import random
import logging

logger = logging.getLogger(__name__)

class SledgeCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.load_sledge_statements()

    def load_sledge_statements(self):
        """Load sledge statements from JSON file"""
        try:
            with open('data/sledge_statements.json', 'r') as f:
                self.sledge_statements = json.load(f)
            logger.info("Sledge statements loaded successfully")
        except Exception as e:
            logger.error(f"Error loading sledge statements: {e}")
            self.sledge_statements = {
                "batter": ["Default batter sledge"],
                "bowler": ["Default bowler sledge"]
            }

    @commands.Cog.listener()
    async def on_message(self, message):
        # Ignore messages from the bot itself
        if message.author == self.bot.user:
            return

        # Handle "hi" messages
        if message.content.lower().startswith('hi'):
            await message.channel.send(f'Hi {message.author.name}!')

        # Handle cricket bot messages
        if message.author.id == 1133475416338866276:
            content = message.content.lower()

            if "**is out**" in content:
                embed = discord.Embed(
                    description="Come on boys, let's rip through this tail",
                    color=discord.Color.random()
                )
                await message.channel.send(embed=embed)

            elif "defended" in content:
                sledge = random.choice(self.sledge_statements["batter"])
                embed = discord.Embed(
                    description=sledge,
                    color=discord.Color.random()
                )
                await message.channel.send(embed=embed)

            elif "**metres**" in content:
                sledge = random.choice(self.sledge_statements["bowler"])
                embed = discord.Embed(
                    description=sledge,
                    color=discord.Color.random()
                )
                await message.channel.send(embed=embed)

    @app_commands.command(
        name="sledge_batter",
        description="Send a sledge to a batter"
    )
    async def sledge_batter(
        self, 
        interaction: discord.Interaction, 
        target: discord.Member = None
    ):
        """Sledge a batter"""
        await self._send_sledge(interaction, "batter", target)

    @app_commands.command(
        name="sledge_bowler",
        description="Send a sledge to a bowler"
    )
    async def sledge_bowler(
        self, 
        interaction: discord.Interaction, 
        target: discord.Member = None
    ):
        """Sledge a bowler"""
        await self._send_sledge(interaction, "bowler", target)

    async def _send_sledge(
        self, 
        interaction: discord.Interaction, 
        player_type: str, 
        target: discord.Member = None
    ):
        """Helper method to send sledges"""
        try:
            sledge = random.choice(self.sledge_statements[player_type])
            target_mention = target.mention if target else "someone"
            
            embed = discord.Embed(
                description=f"{interaction.user.mention} sledges {target_mention}:\n{sledge}",
                color=discord.Color.random()
            )
            
            await interaction.response.send_message(embed=embed)
            logger.info(f"Sledge sent by {interaction.user} to {target if target else 'no target'}")
        except Exception as e:
            logger.error(f"Error sending sledge: {e}")
            await interaction.response.send_message(
                "Sorry, something went wrong while sending the sledge!",
                ephemeral=True
            ) 