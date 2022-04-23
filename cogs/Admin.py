import discord

from discord.ext import commands
from discord import app_commands
from discord import Permissions


class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.dir_aliases = {
            'b': 'before',
            'up': 'before',
            'u': 'before',
            'a': 'after',
            'down': 'after',
            'd': 'after',
        }

    # kicks member
    @app_commands.command(name="kick")
    @app_commands.guilds(discord.Object(id=658947832392187906))
    @commands.has_permissions(kick_members=True)
    async def kick(self, i: discord.Interaction, user: discord.Member, *, reason:str=None):
        if user.top_role > i.user.top_role:
            return await i.response.send_message(f"You can't kick this person, I suppose!")
        await user.kick(reason=reason)
        return await i.response.send_message(f"{user} has been yeeted, I suppose!")

    # bans member
    @app_commands.command(name="ban")
    @app_commands.guilds(discord.Object(id=658947832392187906))
    @commands.has_permissions(ban_members=True)
    async def ban(self, i: discord.Interaction, user: discord.Member, *, reason:str=None):
        if user.top_role > i.user.top_role:
            return await i.response.send_message(f"You can't ban this person, I suppose!")
        await user.ban(reason=reason)
        await i.response.send_message(f"{user} has been yeeted forever, I suppose!")

    @kick.error
    async def kick_error(self, error, ctx):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to do that, I suppose!")

    @ban.error
    async def ban_error(self, error, ctx):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to do that, I suppose!")

    # unbans user
    @app_commands.command(name="unban")
    @app_commands.guilds(discord.Object(id=658947832392187906))
    @commands.has_permissions(ban_members=True)
    async def unban(self, i: discord.Interaction, *, member: discord.User):
        await i.guild.unban(member)
        await i.response.send_message(f"{member} has been unbanned, I suppose!")

    @unban.error
    async def unban_error(self, error, ctx):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to do that, I suppose!")

    # clears chat
    @app_commands.command(name="clean")
    @app_commands.guilds(discord.Object(id=658947832392187906))
    @commands.has_permissions(administrator=True)
    async def clean(self, i: discord.Interaction, limit: int, direction: str = None, msg_id: int = None):
        direction = self.dir_aliases[direction] if direction in self.dir_aliases else direction

        if (msg_id):
            msg = await i.channel.fetch_message(msg_id)
            if direction == "after":
                history = await i.channel.history(limit=limit, after=msg, oldest_first=True).flatten()
            elif direction == "before":
                history = await i.channel.history(limit=limit, before=msg, oldest_first=False).flatten()
            for message in set(history):
                await message.delete()
        elif (direction == "after"):
            return await i.send("I can't delete future messages, in fact! Tell me which message you want me to start deleting from, I suppose!")
        elif (direction == "before"):
            history = await i.channel.history(limit=limit, before=ctx.message, oldest_first=False).flatten()
            for message in set(history):
                await message.delete()
        else:
            await i.channel.purge(limit=limit)

        await i.response.send_message('Cleared by {}, I suppose!'.format(i.user.mention))

    # deletes a member's all messages
    @app_commands.command(name="purge")
    @app_commands.guilds(discord.Object(id=658947832392187906))
    @commands.has_permissions(administrator=True)
    async def purge(self, i: discord.Interaction, member: discord.Member = None):
        if member == self.bot.user:
            await i.response.send_message("Nope, in fact!")
        elif member:
            async for message in i.channel.history(oldest_first=False):
                if message.author == member:
                    await message.delete()
            await i.response.send_message(f'I have cleansed this channel of {member.mention}\'s messages, in fact!')
        else:
            await i.response.send_message("Which degenerate's messages do you want to yeet, I suppose?!")

    # print the joined servers in the logs
    @commands.command()
    @commands.is_owner()
    async def servers(self, ctx):
        print(f'Logged in as: {self.bot.user.name}\n')
        print(f'Server List ({len(self.bot.guilds)})\n')
        server_counter = 1
        for guild in set(self.bot.guilds):
            print(
                f"{server_counter}. {guild.name}, owned by {guild.owner} with {guild.member_count} members")
            server_counter += 1

    # terminates the bot
    @commands.command(aliases=["kill"])
    @commands.is_owner()
    async def terminate(self, ctx):
        await ctx.send("Betty goes offline, I suppose!")
        await self.bot.close()

    # toggles commands
    @commands.command()
    @commands.is_owner()
    async def toggle(self, ctx, cmd):
        cmd = self.bot.get_command(cmd)

        if ctx.command == cmd:
            await ctx.reply("Wait, that's illegal, I suppose!")
        else:
            cmd.enabled = not cmd.enabled
            status = "enabled" if cmd.enabled else "disabled"
            await ctx.send(f"I have {status} the `{cmd.qualified_name}` command, in fact!")


async def setup(bot: commands.Bot):
    await bot.add_cog(Admin(bot))
