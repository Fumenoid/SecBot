import discord
from discord.ext import commands
#from dotenv import load_dotenv
import asyncio
import sys
import os
import random
import helpembed
import configfile

#load_dotenv()

bot = commands.Bot(command_prefix=str(os.environ.get('command_prefix')), case_insensitive=True)  # bot command prefix
bot.remove_command('help')
# Loading Cogs

extensions = ['moderation', 'general']

if __name__ == '__main__':
    sys.path.insert(1, os.getcwd() + '/cogs/')
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load cogs : {e}')


# EVENTS

# Event: when bot becomes ready.
@bot.event  # event/function decorators
async def on_ready():
    print('Bot is ready')  # message which bot sends when it is ready

# Using Events for Logging too, should i make a seperate cog for it ? maybe later
# Event: when any member joins the server
@bot.event
async def on_member_join(member):  # a function which works when any member joins,need param `member`
    print(f'{member} has joined the server :)')
    channel = discord.utils.get(member.guild.channels, name='honk-the-planet') # bot-commands
    bchannel = discord.utils.get(member.guild.channels, name='bot-commands')
    await channel.send(
        f'**Hey there, {member.mention} Welcome to UPES Security Discord!**\n\n'
        f'If you are new to discord here are some things that will help you get started...\n'
        f'First, Discord is just another chat platform just properly organised and have bots _like i am_ :D\n'
        f'Secound, go to {bchannel.mention} and type `$channeldesc`, you will get a list of all channels(chat rooms) and why we have them'
        f'\n\nHappy hacking :D')
    role = discord.utils.get(member.guild.roles, name='h4cK0r5')
    await member.add_roles(role)


# On error Event
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command. Please use `$help` to know list current valid commands.')
    else:
        await ctx.send(
            f'An error occurred. Please use `{bot.command_prefix}reportbot <Error>`, gaaliya do lazy bot creator ko')


# JHDbot help message
@bot.command(name="help")  # alias of command name
async def _help(ctx, helprole=None):  # role-vise help section
    role = discord.utils.get(ctx.author.roles, name='Veteran')
    cool_people = discord.utils.get(ctx.author.roles, name='Cool People')
    if (str(
            ctx.message.channel) == 'bot-commands' or role is not None or cool_people is not None
            or ctx.message.author.guild_permissions.manage_messages):
        if helprole == 'Moderator' or helprole == 'moderator':
            emb = discord.Embed(description=helpembed.moderator_help_list, colour=0x844DB9)
            await attach_embed_info(ctx, emb)
            await ctx.send(embed=emb)
        else:
            emb = discord.Embed(title='Upes Sec Team', url='https://www.upes.ac.in',
                                description=helpembed.memberhelplist, color=0x844DB9)
            await attach_embed_info(ctx, emb)
            await ctx.send(embed=emb)
    else:
        await ctx.send('Please use this command in `#bot-commands`')


# Channel desc messages
@bot.command(aliases=['chdesc', 'channeldesc'])
async def channel_desc(ctx):
    if (str(ctx.message.channel) == 'bot-commands' or ctx.message.author.guild_permissions.manage_messages):
        emb = discord.Embed(description=helpembed.channels, colour=0x844DB9)
        await attach_embed_info(ctx, emb)
        await ctx.message.author.send(embed=emb)
    else:
        await ctx.send('Please use this command in `#bot-commands`')


async def attach_embed_info(ctx=None, embed=None):
    embed.set_author(name='SecBot', icon_url=f'{ctx.guild.icon_url}')
    embed.set_thumbnail(url=f'{ctx.guild.icon_url}')
    embed.set_footer(text='by: UpesSecTeam')
    return embed

# Token
bot.run(str(os.environ.get('bot_token')))  # token
#bot.run(configfile.bot_token)