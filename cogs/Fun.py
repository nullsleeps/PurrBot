import discord
from discord.ext import commands
import jokes
import asyncio
import os
import random

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Purr~ Fun System Online")
    
    @commands.command()
    async def bing(self, ctx):
     boo_embed = discord.Embed(title="PURR~!", description="Did I scare ya?", color=discord.Color.pink())
     boo_embed.add_field(name=f"{self.bot.user.name}'s PURRtancy (ms): ", value=f"{round(self.bot.latency * 1000)} Purrs per second", inline=False)
     boo_embed.set_footer(text="Purrzz", icon_url=self.bot.user.avatar)
     await ctx.send(embed=boo_embed)

    @commands.command()
    async def meow(self, ctx):
     await ctx.send('meoww')

    @commands.command()
    async def joke(self, ctx):
     joke = jokes.get_joke()
     await ctx.send(joke)

    @commands.command(aliases=["HELP", "Help", "911", "Ambulance", "call 911"])
    async def medicalhelp(self, ctx):
     await ctx.send(f"{ctx.author.mention} Call 911 by yourself you're a big bitch now")

    @commands.command(name="demure")
    async def very(self, ctx):
     await ctx.send("Very Demure")

async def setup(bot):
   await bot.add_cog(fun(bot))