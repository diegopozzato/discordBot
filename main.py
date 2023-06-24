import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from discord_slash import SlashCommand


activity = discord.Activity()
intents = discord.Intents.all()
intents.members = True

Bot_prefix = "."

client = commands.Bot(command_prefix=Bot_prefix, intents=intents, activity=activity)

slash = SlashCommand(client, sync_commands=True)


async def load():
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await client.load_extension(f'cogs.{file[:-3]}')


@client.event
async def on_ready():
    print(client.user.name)
    print('------')
    await load()


load_dotenv()

client.run(os.environ['TOKEN'])
