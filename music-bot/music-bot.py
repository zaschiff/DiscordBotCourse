import discord
from discord.ext import commands
import youtube_dl
import os

intents =  discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)


# Commands

@client.command()
#@commands.has_role(792127632745299998)
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@client.command()
#@commands.has_role(792127632745299998)
async def disconnect(ctx):
    await ctx.voice_client.disconnect()
    await client.change_presence(activity=None)


@client.command()
# @commands.has_role(792127632745299998)
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current song to end or use the 'stop' command.")
        return

    voice = ctx.voice_client

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))

    activity = discord.Activity(
        name="Music",
        type=discord.ActivityType.playing
    )

    await client.change_presence(activity=activity)



@client.command()
#@commands.has_role(792127632745299998)
async def pause(ctx):
    voice = ctx.voice_client
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("The audio is not currently playing.")


@client.command()
#@commands.has_role(792127632745299998)
async def resume(ctx):
    voice = ctx.voice_client
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command()
#@commands.has_role(792127632745299998)
async def stop(ctx):
    voice = ctx.voice_client
    voice.stop()


# Error Handlers

@join.error
async def join_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("You must join a voice channel to use this command.")
    elif isinstance(error, commands.MissingRole):
        await ctx.send("You do not have permission to use this command.")


@disconnect.error
async def disconnect_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("The bot must be in a voice channel to use this command.")
    elif isinstance(error, commands.MissingRole):
        await ctx.send("You do not have permission to use this command.")


@play.error
async def play_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("The bot must be in a voice channel to use this command.")
    elif isinstance(error, commands.MissingRole):
        await ctx.send("You do not have permission to use this command.")


@pause.error
async def pause_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("The bot must be in a voice channel to use this command.")
    elif isinstance(error, commands.MissingRole):
        await ctx.send("You do not have permission to use this command.")


@resume.error
async def resume_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("The bot must be in a voice channel to use this command.")
    elif isinstance(error, commands.MissingRole):
        await ctx.send("You do not have permission to use this command.")


@stop.error
async def stop_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("The bot must be in a voice channel to use this command.")
    elif isinstance(error, commands.MissingRole):
        await ctx.send("You do not have permission to use this command.")



client.run('Your Token')