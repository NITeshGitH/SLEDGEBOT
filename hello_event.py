import discord
from discord.ext import commands
import json
import random

class HelloEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open('sledge_statements.json') as f:
            self.sledge_statements = json.load(f)

    def get_random_color(self):
        return discord.Color(random.randint(0, 0xFFFFFF))

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.author.id == 1133475416338866276:
            content = message.content.lower()

            if "**is out**" in content:
                embed = discord.Embed(
                    description="Come on boys, let's rip through this tail",
                    color=self.get_random_color()
                )
                await message.channel.send(embed=embed)

            elif "defended" in content:
                sledge = random.choice(self.sledge_statements["batter"])
                embed = discord.Embed(
                    description=sledge,
                    color=self.get_random_color()
                )
                await message.channel.send(embed=embed)

            elif "**metres**" in content:
                sledge = random.choice(self.sledge_statements["bowler"])
                embed = discord.Embed(
                    description=sledge,
                    color=self.get_random_color()
                )
                await message.channel.send(embed=embed)

        if message.content.lower().startswith('hi'):
            await message.channel.send(f'Hi {message.author.name}!')
