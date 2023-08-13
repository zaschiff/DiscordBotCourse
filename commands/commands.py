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

@bot.command()
async def server(ctx):
    server_naame        = ctx.guild.name
    server_dsc          = ctx.guild.description
    server_region       = ctx.guild.preferred_locale
    server_icon         = ctx.guild.icon
    server_member_count = ctx.guild.member_count
    server_owner        = str(ctx.guild.owner)

    server_embed = discord.Embed(
        title= server_naame + " Server Infromation",
        description=server_dsc,
        color=discord.Color.blurple(),
    )
    server_embed.add_field(name="Owner", value=server_owner, inline=True)
    server_embed.add_field(name="Region", value=server_region, inline=True)
    server_embed.add_field(name="Member Count", value=server_member_count, inline=True)

    await ctx.send(embed=server_embed)

bot.run('YOUR BOT TOKEN')