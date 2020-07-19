import discord
from discord.ext import commands
import asyncio
import urllib

class GeneralCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Ping Command to check if server is up or not
    @commands.command()
    # creating Commands ctx is something like context, send automatically
    async def ping(self, ctx):
        if (str(
                ctx.message.channel) == "bot-commands"
                or ctx.message.author.guild_permissions.manage_messages):
            await ctx.send(f'Ping - {round(self.bot.latency * 1000)}ms')
        else:
            await ctx.send('Please use this command in `#bot-commands`')


    # Report bot command
    @commands.command(aliases=['reportbot'])
    async def report_bot(self, ctx, *, reason=None):
        if (str(
                ctx.message.channel) == "bot-commands" or ctx.message.author.guild_permissions.manage_messages):
            if reason == None:
                await ctx.send("Invalid syntax, please add the issue you are facing.")
            else:
                creator = await self.bot.fetch_user(554907015785218050)
                await creator.send(f"Reported by user {ctx.message.author} : " + reason)
                await ctx.send("Your report has been successfully forwarded to moderators")
        else:
            await ctx.send("Please use this command in `#bot-commands`")

    # reporting users
    @commands.command()
    async def report(self, ctx, user=None, *, reason=None):
        if (str(
                ctx.message.channel) == "bot-commands" 
                or ctx.message.author.guild_permissions.manage_messages):
            if reason is None or user is None:
                await ctx.send(f'Invalid syntax, please check `{self.bot.command_prefix}help` to check the syntax and '
                               f'pass proper arguments.')
            else:
                channel = discord.utils.get(ctx.message.author.guild.channels, name="moderators-chat")
                await channel.send(f'Reported by user {ctx.message.author.mention} : Complain against user {user} - ' + reason)
                await ctx.send('Your report has been successfully forwarded to moderators')
        else:
            await ctx.send('Please use this command in `#bot-commands`')

    # reporting to admins
    @commands.command(aliases=['adminsupport'])
    async def report_to_admins(self, ctx, *, reason=None):
        if (str(
                ctx.message.channel) == "bot-commands" 
                or ctx.message.author.guild_permissions.manage_messages):
            if reason is None:
                await ctx.send(f'Invalid syntax, please check `{self.bot.command_prefix}help` to check the syntax and '
                               f'pass proper arguments.')
            else:
                channel = discord.utils.get(ctx.message.author.guild.channels, name="administrator-chat")
                await channel.send(f'A request/report by user {ctx.message.author.mention} : {reason}')
                await ctx.send('Your report/request has been successfully forwarded to Admins')
        else:
            await ctx.send('Please use this command in `#bot-commands`')

    @commands.command(aliases=['lmgtfy'])
    async def _lmgtfy(self, ctx, *, input):
        if ctx.message.author.guild_permissions.manage_messages:
            lmgtfyurl = 'https://lmgtfy.com/?q='
            fullyurl = lmgtfyurl + urllib.parse.quote_plus(input, safe='')
            await ctx.send(fullyurl)
        else:
            await ctx.send('Seems like you are not authorized to use this command D:')

def setup(bot):
    bot.add_cog(GeneralCog(bot))
    print('General cog loaded')
