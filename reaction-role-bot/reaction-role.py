import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_raw_reaction_add(payload):
    payload_message_id = payload.message_id
    target_message_id = 1140091535644442644
    guild_id = payload.guild_id
    guild = client.get_guild(guild_id)

    if payload_message_id == target_message_id:
        emoji_choice = str(payload.emoji.name)
        # print(str(payload.emoji.name))
        if emoji_choice == '\U0001f603':
            # smiley reacted, give that person happy role
            role = discord.utils.get(guild.roles, name='Happy')
            await payload.member.add_roles(role)
            # print('reacted with smiley')
        elif emoji_choice == '\U0001f62d':
            role = discord.utils.get(guild.roles, name='Sad')
            await payload.member.add_roles(role)
            # print('reacted with sob')
        elif emoji_choice == '\U0001f60e':
            role = discord.utils.get(guild.roles, name='Cool')
            await payload.member.add_roles(role)
            # print('reacted with sunglasses')

@client.event
async def on_raw_reaction_remove(payload):
    payload_message_id = payload.message_id
    target_message_id = 1140091535644442644
    guild_id = payload.guild_id
    guild = client.get_guild(guild_id)

    if payload_message_id == target_message_id:
        member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
        emoji_choice = str(payload.emoji.name)
        # print(str(payload.emoji.name))
        if emoji_choice == '\U0001f603':
            # smiley reacted, give that person happy role
            role = discord.utils.get(guild.roles, name='Happy')
            await member.remove_roles(role)
            # print('reacted with smiley')
        elif emoji_choice == '\U0001f62d':
            role = discord.utils.get(guild.roles, name='Sad')
            await member.remove_roles(role)
            # print('reacted with sob')
        elif emoji_choice == '\U0001f60e':
            role = discord.utils.get(guild.roles, name='Cool')
            await member.remove_roles(role)
            # print('reacted with sunglasses')

client.run('')