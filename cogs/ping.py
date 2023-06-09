import discord
import discord.utils
import asyncio
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hello(self, ctx): # all methods now must have both self and ctx parameters
        await ctx.send('Hello!')


async def setup(client):
    await client.add_cog(Ping(client))
