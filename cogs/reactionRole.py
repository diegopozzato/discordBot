import discord
from discord import app_commands
from discord.ext import commands
import asyncio

class Profile:
    def __init__(self, message_id, role=[], emoji_id=[]):
        self.message_id = message_id
        self.role = role
        self.emoji_id = emoji_id
        pass


Profile_list = []


class ReactionRole(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(manage_roles=True)
    @commands.command(pass_context=True)
    async def rreaction(self, ctx, msgID: int, *args):
        role = []
        emoji_id = []
        guild_id = ctx.guild.id
        guild = self.client.get_guild(guild_id)

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
                reaction, user = await self.client.wait_for(
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

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, event):
        if event.user_id == self.client.user.id:
            return
        if Profile_list:
            pass
        else:
            return

        payload_message_id = event.message_id
        guild_id = event.guild_id
        guild = self.client.get_guild(guild_id)

        for x in range(len(Profile_list)):
            if Profile_list[x].message_id == payload_message_id:
                i = x

        try:
            i
        except NameError:
            return

        for y in range(len(Profile_list[i].emoji_id)):
            if event.emoji == Profile_list[i].emoji_id[y]:
                temp = Profile_list[i].role[y]
                src_role_1 = filter(str.isdigit, temp)
                src_role_2 = "".join(src_role_1)
                role = discord.utils.get(guild.roles, id=int(src_role_2))
                try:
                    await event.member.add_roles(role)
                except Exception as ex:
                    print("error")
                else:
                    pass
            elif event.emoji.name == Profile_list[i].emoji_id[y]:
                temp = Profile_list[i].role[y]
                src_role_1 = filter(str.isdigit, temp)
                src_role_2 = "".join(src_role_1)
                role = discord.utils.get(guild.roles, id=int(src_role_2))
                try:
                    await event.member.add_roles(role)
                except Exception as ex:
                    print("error")
                else:
                    pass
            else:
                pass


async def setup(client):
    await client.add_cog(ReactionRole(client))
