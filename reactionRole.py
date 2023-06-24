import discord
import discord.utils
import numpy as np
import asyncio
import re
import string
from discord.ext import commands
#intents = discord.Intents.default()
intents = discord.Intents.all()
intents.members = True
Bot_prefix = "."
activity = discord.Activity(name='🤍🤍🤍', type=discord.ActivityType.watching)
client = commands.Bot(command_prefix=Bot_prefix, intents=intents, activity=activity)
client.remove_command("help")

#Python interpreter 3.10

class Profile:
    def __init__(self, message_id, role=[], emoji_id=[]):
        self.message_id = message_id
        self.role = role
        self.emoji_id = emoji_id
        pass

Profile_list=[]

@client.event
async def on_ready():
    print("Im Online!")

'''
#REACTION ROLE APPLICATION
@commands.has_permissions(manage_roles=True)
@client.command(pass_context=True)
async def rreaction(ctx, msgID: int, *args):
    role = []
    emoji_id = []
    guild_id = ctx.guild.id
    guild = client.get_guild(guild_id)

    for arg in args:
        if "@" in arg:
            role.append(arg)
        else:
            embed = discord.Embed(title="❌ CommandMentionError", description=".rreaction <messageId> <@role> <@role> ...", color=0xC53131)
            return await ctx.send(embed=embed)

    for i in role:
        embed = discord.Embed(color=0x2A69CB, description="React with the emoji you want")
        embed.add_field(name="Emoji for:", value=i)
        role_message = await ctx.send(embed=embed)
        role_message_id = role_message.id

        try:
            reaction, user = await client.wait_for(
                'reaction_add',
                timeout=30.0,
                check=lambda reaction, user: reaction.message.id == role_message_id
            )
        except asyncio.TimeoutError:
            embed = discord.Embed(title="⌛ Error - Time's up", color=0xCDDC33)
            await ctx.reply(embed=embed, mention_author=False)
            return
        except asyncio.CheckError:
            return
        else:
            try:
                msg = await ctx.fetch_message(msgID)
            except Exception as ex:
                embed1 = discord.Embed(title="#Error - TargetMessageId", description="1)Make sure the message-id is correct\n2)Make sure you are in the same channel as the message-id", color=0xC53131)
                embed1.add_field(name="Emoji for:", value='❌ ' + i)
                await role_message.edit(embed=embed1)
                return
            else:
                await msg.add_reaction(reaction.emoji)
                emoji_id.append(reaction.emoji)
                embed1 = discord.Embed(color=0x3BCC39)
                embed1.add_field(name="Emoji for:", value='✅ '+i)
                await role_message.edit(embed=embed1)
                pass

    Profile_list.append(Profile(msgID, role, emoji_id))
'''

#ADD REACTION
@client.event
async def on_raw_reaction_add(payload):
    if payload.user_id == client.user.id:
        return
    if Profile_list:
        pass
    else:
        return

    payload_message_id = payload.message_id
    guild_id = payload.guild_id
    guild = client.get_guild(guild_id)

    for x in range(len(Profile_list)):
        if Profile_list[x].message_id == payload_message_id:
            i = x

    try:
        i
    except NameError:
        return

    for y in range(len(Profile_list[i].emoji_id)):
        if payload.emoji == Profile_list[i].emoji_id[y]:
            temp = Profile_list[i].role[y]
            src_role_1 = filter(str.isdigit, temp)
            src_role_2 = "".join(src_role_1)
            role = discord.utils.get(guild.roles, id=int(src_role_2))
            try:
                await payload.member.add_roles(role)
            except Exception as ex:
                print("error")
            else:
                pass
        elif payload.emoji.name == Profile_list[i].emoji_id[y]:
            temp = Profile_list[i].role[y]
            src_role_1 = filter(str.isdigit, temp)
            src_role_2 = "".join(src_role_1)
            role = discord.utils.get(guild.roles, id=int(src_role_2))
            try:
                await payload.member.add_roles(role)
            except Exception as ex:
                print("error")
            else:
                pass
        else:
            pass

#REMOVE REACTION
@client.event
async def on_raw_reaction_remove(payload):
    if payload.user_id == client.user.id:
        return
    if Profile_list:
        pass
    else:
        return

    payload_message_id = payload.message_id
    guild_id = payload.guild_id
    guild = client.get_guild(guild_id)

    for x in range(len(Profile_list)):
        if Profile_list[x].message_id == payload_message_id:
            i = x

    try:
        i
    except NameError:
        return

    for y in range(len(Profile_list[i].emoji_id)):
        if payload.emoji == Profile_list[i].emoji_id[y]:
            temp = Profile_list[i].role[y]
            src_role_1 = filter(str.isdigit, temp)
            src_role_2 = "".join(src_role_1)
            role = discord.utils.get(guild.roles, id=int(src_role_2))
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            try:
                await member.remove_roles(role)
            except Exception as ex:
                print("error")
            else:
                pass
        elif payload.emoji.name == Profile_list[i].emoji_id[y]:
            temp = Profile_list[i].role[y]
            src_role_1 = filter(str.isdigit, temp)
            src_role_2 = "".join(src_role_1)
            role = discord.utils.get(guild.roles, id=int(src_role_2))
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            try:
                await member.remove_roles(role)
            except Exception as ex:
                print("error")
            else:
                pass
        else:
            pass

#REMOVE OBJECT ON MESSAGE DELETE
@client.event
async def on_raw_message_delete(payload):
    message_id = payload.message_id
    for i in range(len(Profile_list)):
        if message_id == Profile_list[i].message_id:
            Profile_list.remove(Profile_list[i])

#HELP COMMAND
@client.command()
async def help(ctx):
    await print("ciao")


client.run("TOKEN")