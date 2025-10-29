import discord
from discord import app_commands
from discord.ext import commands
import json
import random
import os
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class SledgeCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.load_sledge_statements()

    def load_sledge_statements(self):
        try:
            with open('data/sledge_statements.json', 'r') as f:
                self.sledge_statements = json.load(f)
            logger.info("Sledge statements loaded successfully")
        except Exception as e:
            logger.error(f"Error loading sledge statements: {e}")
            self.sledge_statements = {
                "batter": [{"text": "Default batter sledge", "gif": "https://raw.githubusercontent.com/WrestGit/gif/refs/heads/main/lol.gif"}],
                "bowler": [{"text": "Default bowler sledge", "gif": "https://raw.githubusercontent.com/WrestGit/gif/refs/heads/main/lol.gif"}]
            }

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.content.lower().startswith('hi'):
            await message.channel.send(f'Hi {message.author.name}!')

        if message.author.id == 814100764787081217:
            await self._handle_cricket_bot_message(message)

        await self.bot.process_commands(message)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if after.author == self.bot.user:
            return
        
        if after.author.id == 814100764787081217:
            if before.content != after.content:
                await self._handle_cricket_bot_message(after)

    # Create a command group named "sledge"
    sledge = app_commands.Group(name="sledge", description="Sledge a player")

    @sledge.command(
        name="batter",
        description="Send a sledge to a batter"
    )
    async def batter(
        self, 
        interaction: discord.Interaction, 
        target: Optional[discord.User] = None
    ):
        await self._send_sledge(interaction, "batter", target)

    @sledge.command(
        name="bowler",
        description="Send a sledge to a bowler"
    )
    async def bowler(
        self, 
        interaction: discord.Interaction, 
        target: Optional[discord.User] = None
    ):
        await self._send_sledge(interaction, "bowler", target)

    async def _send_sledge(
        self, 
        interaction: discord.Interaction, 
        player_type: str, 
        target: Optional[discord.User] = None
    ):
        try:
            if target:
                if target.id == interaction.user.id:
                    await interaction.response.send_message("Sledging yourself? That's a bit sad, mate.", ephemeral=False)
                    return

                assert self.bot.user is not None
                if target.id == self.bot.user.id:
                    await interaction.response.send_message("You can't sledge me, I'm on your side!", ephemeral=False)
                    return
                
                if target.bot:
                    await interaction.response.send_message("You can't sledge a bot! Find a real person to sledge.", ephemeral=False)
                    return

            sledge = random.choice(self.sledge_statements[player_type])
            target_mention = target.mention if target else "someone"
            
            embed = discord.Embed(
                description=sledge['text'],
                color=discord.Color.random()
            )
            embed.set_image(url=sledge['gif'])
            
            await interaction.response.send_message(
                f"{interaction.user.mention} sledges {target_mention}!",
                embed=embed
            )
            logger.info(f"Sledge sent by {interaction.user} to {target if target else 'no target'}")
        except Exception as e:
            logger.error(f"Error sending sledge: {e}")
            await interaction.response.send_message(
                "Sorry, something went wrong while sending the sledge!",
                ephemeral=True
            ) 

    async def _handle_cricket_bot_message(self, message: discord.Message):
        logger.debug(f"Handling message from cricket bot: {message.content}")
        content = message.content

        if "**IS OUT**" in content:
            embed = discord.Embed(
                description="Come on boys, let's rip through this tail",
                color=discord.Color.random()
            )
            await message.channel.send(embed=embed)

        elif "defended" in content.lower():
            sledge_data = random.choice(self.sledge_statements["batter"])
            embed = discord.Embed(
                description=sledge_data['text'],
                color=discord.Color.random()
            )
            embed.set_image(url=sledge_data['gif'])
            await message.channel.send(embed=embed)

        elif "**metres**" in content:
            sledge_data = random.choice(self.sledge_statements["bowler"])
            embed = discord.Embed(
                description=sledge_data['text'],
                color=discord.Color.random()
            )
            embed.set_image(url=sledge_data['gif'])
            await message.channel.send(embed=embed)
