import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('The bot is online')

@client.event
async def on_message(msg):
    # print(msg.author)
    if msg.author == client.user:
        return
    if str(msg.author) == 'xzjewboysx' and str(msg.content).lower() == 'hello':
        await msg.channel.send('Shh the admin is watching!')
    elif str(msg.content).lower() == 'hello':
        await msg.channel.send('hello')

    if str(msg.content).lower() == 'hi mr.bot!':
        await msg.add_reaction('\U0001f44b')

@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(str(user) + ' reacted with ' + reaction.emoji)

@client.event
async def on_message_edit(before, after):
    if str(before.author) == str(after.author):
        await before.channel.send(str(before.author) + ' has edited their message')
    else:
        await before.channel.send(str(after.author) + ' has edited ' + str(before.author) + "'s message")
    
    await before.channel.send('Before: '+ str(before.content))
    await before.channel.send('After: ' + str(after.content))


client.run('MTE0MDA1OTcyMTgwMjQ0OTAxOA.GdqWvE.bQI1joxGMW3oBa88UXENlrI-EGCvLSX2qPjSWs')