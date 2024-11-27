import discord
from discord.ext import commands
import json
import random
from discord import app_commands

@app_commands.guild_only()
class SledgeCommand(commands.GroupCog, group_name="sledge"):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
        with open('sledge_statements.json') as f:
            self.sledge_statements = json.load(f)

    @app_commands.command(name="tobatter", description="Sends a random sledge to a batter")
    async def sledgetobatter(self, interaction: discord.Interaction, user: discord.User = None):
        mentioned_user = user.mention if user else ""
        sledge = self.get_random_sledge("batter")
        embed = discord.Embed(
            description=f'{interaction.user.mention} sledges {mentioned_user} {sledge}',
            color=self.get_random_color()
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="tobowler", description="Sends a random sledge to a bowler")
    async def sledgetobowler(self, interaction: discord.Interaction, user: discord.User = None):
        mentioned_user = user.mention if user else ""
        sledge = self.get_random_sledge("bowler")
        embed = discord.Embed(
            description=f'{interaction.user.mention} sledges {mentioned_user} {sledge}',
            color=self.get_random_color()
        )
        await interaction.response.send_message(embed=embed)

    def get_random_sledge(self, player_type):
        statements = self.sledge_statements[player_type]
        return random.choice(statements)

    def get_random_color(self):
        return discord.Color(random.randint(0, 0xFFFFFF))

async def setup(bot):
    await bot.add_cog(SledgeCommand(bot))
