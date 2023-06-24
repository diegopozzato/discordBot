import discord
from discord import app_commands
from discord.ext import commands


class Data(commands.Cog):
    def __init__(self, client):
        self.client = client




async def setup(client):
    await client.add_cog(Data(client))
