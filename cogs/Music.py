import discord
from discord.ext import commands


class Music(commands.Cog):
    def init(self, client):
        self.client = client

    @commands.command(name="join", aliases=["enter", "j"])
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()


    @commands.command(name="leave", aliases=["disconnect", "l"])
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()


async def setup(client):
    await client.add_cog(Music(client))