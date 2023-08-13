import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed_help_list = discord.Embed(
        title = 'dbcp-bot Commands',
        description = "All bot commands listed below.",
        color = discord.Color.blue()
    )
    embed_help_list.set_author(name="Zach Schiff")
    embed_help_list.add_field(name="!help", value="lists all bot commands",  inline=True)
    embed_help_list.add_field(name="!hello", value="Sends a hello message.", inline=True)
    embed_help_list.add_field(name="!ping", value="Sends a pong", inline=True)

    await ctx.send(embed=embed_help_list)

@bot.command()
async def hello(ctx):
    await ctx.send("hello")

@bot.command()
async def ping(ctx):
    await ctx.send('Pong')


bot.run('ADD YOUR SECRET TOKEN IN')