import discord
from discord.ext import commands
import os
import random
print(os.listdir('images'))
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def mem(ctx):
    image = random.choice(os.listdir('images'))
    with open (f'images/{image}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem1(ctx):
    with open('images/mem1.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def mem2(ctx):
    with open('images/mem2.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def mem3(ctx):
    with open('images/mem3.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def animal(ctx):
    image = random.choice(os.listdir('animals'))
    with open (f'animals/{image}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def animal1(ctx):
    with open('animals/animal1.webp', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def animal2(ctx):
    with open('animals/animal2.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def animal3(ctx):
    with open('animals/animal3.webp', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def random_facts(ctx):
    image = random.choice(os.listdir('random_facts'))
    with open(f'random_facts/{image}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def plant_facts(ctx):
    image = random.choice(os.listdir('plant_facts'))
    with open(f'plant_facts/{image}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


bot.run('ВАШ ТОКЕН')
