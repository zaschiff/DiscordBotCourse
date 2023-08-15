import json
import os

import discord
from discord.ext import commands


class Economy(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.shop = [['Fedora', 25],
                     ['Gucci Belt', 750]]
        
    async def update_data(self, users, user):
        if str(user.id) not in users:
            users[str(user.id)] = {}
            users[str(user.id)]['experience'] = 0
            users[str(user.id)]['level'] = 1
            users[str(user.id)]['balance'] = 100
            users[str(user.id)]['wage'] = 1
            users[str(user.id)]['inventory'] = []
        try:
            print(users[str(user.id)]['balance'])
        except KeyError:
            users[str(user.id)]['balance'] = 100
            users[str(user.id)]['wage'] = 1
            users[str(user.id)]['inventory'] = []


    async def add_money(self, users, user, wage):
        users[str(user.id)]['balance'] += wage

    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open(r'xp-bot\data\users.json', 'r') as f:
            users = json.load(f)
        
        await self.update_data(users, member)

        with open(r'xp-bot\data\users.json', 'w') as f:
            json.dump(users, f)

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author == self.client.user:
            return
        if msg.content.startswith('!'):
            return
        
        with open(r'xp-bot\data\users.json', 'r') as f:
            users = json.load(f)
        
        await self.update_data(users, msg.author)
        await self.add_money(users, msg.author, users[str(msg.author.id)]['wage'])

        with open(r'xp-bot\data\users.json', 'w') as f:
            json.dump(users, f)

    @commands.command()
    async def wage(self, ctx, member: discord.Member, amount: int):
        with open(r'xp-bot\data\users.json', 'r') as f:
            users = json.load(f)

        await self.update_data(users, member)

        users[str(member.id)]['wage'] = amount

        with open(r'xp-bot\data\users.json', 'w') as f:
            json.dump(users, f)

    @commands.command()
    async def bank(self, ctx):
        with open(r'xp-bot\data\users.json', 'r') as f:
            users = json.load(f)

        await self.update_data(users, ctx.author)

        await ctx.send(f"Name: {ctx.author.mention}\n"
                       f"Balance: ${users[str(ctx.author.id)]['balance']}\n"
                       f"wage: ${users[str(ctx.author.id)]['wage']}/message")
        
        with open(r'xp-bot\data\users.json', 'w') as f:
            json.dump(users, f)
        
    @commands.command()
    async def inventory(self, ctx):
        with open(r'xp-bot\data\users.json', 'r') as f:
            users = json.load(f)

        await self.update_data(users, ctx.author)

        await ctx.send(f"{ctx.author.mention}'s inventory:\n"
                       f"{users[str(ctx.author.id)]['inventory']}")
        
        with open(r'xp-bot\data\users.json', 'w') as f:
            json.dump(users, f)

    @commands.command()
    async def shop(self, ctx):
        print("entered shop command")
        string = ""
        i = 0
        for item in self.shop:
            string += f"{i}. {item[0]} for ${item[1]}\n"
            i += 1

        await ctx.send(string)

    @commands.command()
    async def buy(self, ctx, item: int):
        with open(r'xp-bot\data\users.json', 'r') as f:
            users = json.load(f)

        if self.shop[item - 1][1] > users[str(ctx.author.id)]['balance']:
            await ctx.send("You don't have enough money for that item.")
        elif item > len(self.shop):
            await ctx.send("this item does not exist")
        else:
            await ctx.send(f'''
                           {ctx.author.mention} purchased a {self.shop[item - 1][0]}
                           for ${self.shop[item -1][1]}. It is in your inventory.
                           ''')
            
            await self.update_data(users, ctx.author)

            users[str(ctx.author.id)]['balance'] -= self.shop[item-1][1]
            users[str(ctx.author.id)]['inventory'].append(self.shop.pop(item-1)[0])

            with open(r'xp-bot\data\users.json', 'w') as f:
                json.dump(users, f)


async def setup(client):
    await client.add_cog(Economy(client))