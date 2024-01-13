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
    print(f'Бот {client.user} запущен!')

@bot.command()
async def d20(ctx, rolls: int):
    if rolls > 4:
        await ctx.reply('Превышен лимит кубиков!')
        return
    for i in range(rolls):
        number = random.randint(1, 20)
        await ctx.reply(f'Кубик d20, выпали числа: **{number}**')
        
@bot.command()
async def d100(ctx, rolls: int):
    if rolls > 4:
        await ctx.reply('Превышен лимит кубиков!')
        return
    for i in range(rolls):
        number = random.randint(1, 100)
        await ctx.reply(f'Кубик d100, выпали числа: **{number}**')
        
@bot.command()
async def d12(ctx, rolls: int):
    if rolls > 4:
        await ctx.reply('Превышен лимит кубиков!')
        return
    for i in range(rolls):
        number = random.randint(1, 12)
        await ctx.reply(f'Кубик d12, выпали числа: **{number}**')
        
@bot.command()
async def d10(ctx, rolls: int):
    if rolls > 4:
        await ctx.reply('Превышен лимит кубиков!')
        return
    for i in range(rolls):
        number = random.randint(0, 9)
        await ctx.reply(f'Кубик d10, выпали числа: **{number}**')
        
@bot.command()
async def d8(ctx, rolls: int):
    if rolls > 4:
        await ctx.reply('Превышен лимит кубиков!')
        return
    for i in range(rolls):
        number = random.randint(1, 8)
        await ctx.reply(f'Кубик d8, выпали числа: **{number}**')
        
@bot.command()
async def d6(ctx, rolls: int):
    if rolls > 4:
        await ctx.reply('Превышен лимит кубиков!')
        return
    for i in range(rolls):
        number = random.randint(1, 6)
        await ctx.reply(f'Кубик d6, выпали числа: **{number}**')
        
@bot.command()
async def d4(ctx, rolls: int):
    if rolls > 4:
        await ctx.reply('Превышен лимит кубиков!')
        return
    for i in range(rolls):
        number = random.randint(1, 4)
        await ctx.reply(f'Кубик d4, выпали числа: **{number}**')

@bot.tree.command(name="d20", description="Кинуть кубик d20.")
async def d20(inter: discord.Interaction, rolls: app_commands.Range[int, 1, 4]):
    for i in range(rolls):
        number = random.randint(1, 20)
        await inter.response.send_message(f'Кубик d20, выпали числа: **{number}**')

bot.run('token here')