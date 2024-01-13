# This example requires the 'message_content' intent.
import random

import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='%', intents=intents)
tree = bot.tree

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot {client.user} ready!')

@bot.command()
async def d20(ctx, rolls: int):
    if rolls > 4:
        await ctx.reply('The dice limit has been exceeded!')
        return
    for i in range(rolls):
        number = random.randint(1, 20)
        await ctx.reply(f'Dice d20, the number dropped out: **{number}**')
        
@bot.command()
async def d100(ctx, rolls: int):
    if rolls > 4:
        await ctx.reply('The dice limit has been exceeded!')
        return
    for i in range(rolls):
        number = random.randint(1, 100)
        await ctx.reply(f'Dice d100, the number dropped out: **{number}**')
        
@bot.command()
async def d12(ctx, rolls: int):
    if rolls > 4:
        await ctx.reply('The dice limit has been exceeded!')
        return
    for i in range(rolls):
        number = random.randint(1, 12)
        await ctx.reply(f'Dice d12, the number dropped out: **{number}**')
        
@bot.command()
async def d10(ctx, rolls: int):
    if rolls > 4:
        await ctx.reply('The dice limit has been exceeded!')
        return
    for i in range(rolls):
        number = random.randint(0, 9)
        await ctx.reply(f'Dice d10, the number dropped out: **{number}**')
        
@bot.command()
async def d8(ctx, rolls: int):
    if rolls > 4:
        await ctx.reply('The dice limit has been exceeded!')
        return
    for i in range(rolls):
        number = random.randint(1, 8)
        await ctx.reply(f'Dice d8, the number dropped out: **{number}**')
        
@bot.command()
async def d6(ctx, rolls: int):
    if rolls > 4:
        await ctx.reply('The dice limit has been exceeded!')
        return
    for i in range(rolls):
        number = random.randint(1, 6)
        await ctx.reply(f'Dice d6, the number dropped out: **{number}**')
        
@bot.command()
async def d4(ctx, rolls: int):
    if rolls > 4:
        await ctx.reply('The dice limit has been exceeded!')
        return
    for i in range(rolls):
        number = random.randint(1, 4)
        await ctx.reply(f'Dice d4, the number dropped out: **{number}**')
        
bot.run('token here')
