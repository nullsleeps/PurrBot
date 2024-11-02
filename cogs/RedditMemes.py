import discord
from discord.ext import commands, tasks
import asyncio
import os
from random import choice
import asyncpraw as praw

class redditmemes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = praw.Reddit(client_id="CdQ7E_27esJHgfseu0OSBw", client_secret="6jMmCpccSWy4Qy5V5CQBNU6OLCKBkA", user_agent="script:random:v1.0 (by u/s3nl)")
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Purr~ Reddit Meme System Online")

    @commands.command()
    async def meme(self, ctx: commands.Context):
        subreddit = await self.reddit.subreddit("memes")
        posts_list = []
        async for post in subreddit.new(limit=40):
            if post.author is not None and any(post.url.endswith(ext) for ext in [".png", ".jpg", ".jpeg", ".gif"]):
                author_name = post.author.name
                posts_list.append((post.url, author_name))
            if post.author is None:
                posts_list.append((post.url, "N/A"))

        if posts_list: 
            random_post = choice(posts_list)
            meme_embed = discord.Embed(title="Meme :cat:", description="memememememem :stuck_out_tongue:", color=discord.Color.random())
            meme_embed.set_author(name=f":smiley_cat: PURRR A Meme Was Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
            meme_embed.set_image(url=random_post[0])
            meme_embed.set_footer(text=f"Purr~ :cat: This post was created by {random_post[1]}", icon_url=None)
            await ctx.send(embed=meme_embed)
        else:
            await ctx.send("Purr~ I was Unable to get the mememe :pensive:")
        if subreddit:
            await self.reddit.subreddit("memes")
        else:
            subreddit.close()

def cog_unload(self):
 self.bot.loop.create_task(self.reddit.close())
async def setup(bot):
   await bot.add_cog(redditmemes(bot))