import datetime
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

def is_me(ctx):
    return ctx.message.author.id == 512004496398745603

@bot.command()
@commands.check(is_me)
async def clear(ctx, amount, month=None, day=None, year=None):
    # print("Clear command called")
    if amount == '-':
        # print("Amount = none")
        amount = None
    else:
        # print("Amount != none")
        amount = int(amount) + 1

    if month == None or day == None or year == None:
        # print("Date = none")
        date = None
    else:
        date  =  datetime.datetime(int(year), int(month), int(day))
        # print("Date = " + str(date))

    await ctx.channel.purge(limit=amount, after=date)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You dont have permissions to use this command.")

@bot.command()
async def kick(ctx, member: discord.Member, *, reason):
    await member.kick(reason=reason)

@bot.command()
async def ban(ctx, member: discord.Member, *, reason):
    await member.ban(reason=reason)

@bot.command
async def unban(ctx, *, member):
    banned_list = await ctx.guild.bans()

    for person in banned_list:
        user = person.user
        if member == str(user):
            await ctx.guild.unban(user)



bot.run('Your Bot Token')