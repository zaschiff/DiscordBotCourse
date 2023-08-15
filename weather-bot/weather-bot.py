import discord
import json
import os
import requests
from discord.ext import commands

os.chdir(r'C:\Users\Zachm\OneDrive\Desktop\DiscordBotCourse\weather-bot')
with open(r'data\api-key.json', 'r') as f:
    api_key = json.load(f)


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
@commands.cooldown(2, 1, commands.BucketType.default)
async def weather(ctx, city: str, country: str=None):
    if country:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&units=imperial&appid={api_key['api_key']}"
    else:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={api_key['api_key']}"

    #print(url)

    r = requests.get(url)

    json_data = r.json()

    print(json_data)
    weather = json_data['weather'][0]['main']
    desc = json_data['weather'][0]['description']
    temp = json_data['main']['temp']
    icon = "https://openweathermap.org/img/wn/" + json_data['weather'][0]['icon'] + "@2x.png"
    
    if country:
        location = city + ", " + country
    else:
        location = city

    embed = discord.Embed(
        title="Current Weather",
        description=location,
        color=discord.Color.brand_red()
    )

    embed.set_thumbnail(url=icon)

    embed.add_field(name=weather, value=desc, inline=False)
    embed.add_field(name="Temperature", value=f"{temp}\u2109", inline=False)

    await ctx.send(embed=embed)

@weather.error
async def weather_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("That is not a valid city or country code.")

    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("this command is on cool down.")


bot.run('MTE0MDA1OTcyMTgwMjQ0OTAxOA.G5eMkn.HMIqtj15VKkkuMZmmx8EB0rH4_GkuX_Nn-yduQ')