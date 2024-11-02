import discord
from discord.ext import commands, tasks
import random
import pyjokes
import asyncio
import os
from itertools import cycle

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "purr ", intents=discord.Intents.all())

status = cycle(["Meow", "Purr~", "Playing with Yarn", "Chasing Mice", "meow"])

@tasks.loop(seconds=3600)
async def botstatus():
    await bot.change_presence(activity=discord.Game(next(status)))

@bot.event
async def on_ready():
    print(f'Purr~ Me Ready {bot.user}')
    botstatus.start()

with open("yes.txt") as file:
    yes = file.read()

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load()
        await bot.start(yes)

asyncio.run(main())