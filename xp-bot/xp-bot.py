import discord
import json
import os
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)


save_file_path = r'C:\Users\Zachm\OneDrive\Desktop\DiscordBotCourse\xp-bot\data\users.json'

@client.event
async def on_member_join(member):
    with open(save_file_path, 'r') as f:
        users = json.load(f)
    
    await update_data(users, member)

    with open(save_file_path, 'w') as f:
        json.dump(users, f)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    
    with open(save_file_path, 'r') as f:
        users = json.load(f)
    
    await update_data(users, message.author)
    await add_experience(users, message.author, 5)
    value = await level_up(users, message.author)

    if value:
        await message.channel.send(f'''
            {message.author.mention} 
            has leveled up to level 
            {users[str(message.author.id)]['level']}
        ''')
    
    with open(save_file_path, 'w') as f:
        json.dump(users, f)

    await client.process_commands(message)
@client.command()
async def level(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    
    with open(save_file_path, 'r') as f:
        users = json.load(f)

    level = users[str(member.id)]['level']
    await ctx.send(f"{member.display_name} is level {level}")

@client.command()
async def load(ctx, ext):
    await client.load_extension(f"cogs.{ext}")

@client.command()
async def reload(ctx, ext):
    await client.reload_extension(f"cogs.{ext}")
        
@client.command()
async def unload(ctx, ext):
    await client.unload_extension(f"cogs.{ext}")

async def update_data(users, user):
    if str(user.id) not in users:
        users[str(user.id)] = {}
        users[str(user.id)]['experience'] = 0
        users[str(user.id)]['level'] = 1
        

async def add_experience(users, user, xp):
    users[str(user.id)]['experience'] += xp

async def level_up(users, user):
    exp = users[str(user.id)]['experience']
    level_start = users[str(user.id)]['level']
    level_end = int(exp ** (1/4))

    if level_start < level_end:
        users[str(user.id)]['level'] = level_end
        return True
    else:
        return False

client.run('')

