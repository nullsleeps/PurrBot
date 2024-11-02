import discord
from discord.ext import commands, tasks
import asyncio
import os
from random import choice
import asyncpraw as praw

class redditcats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = praw.Reddit(client_id="CdQ7E_27esJHgfseu0OSBw", client_secret="6jMmCpccSWy4Qy5V5CQBNU6OLCKBkA", user_agent="script:random:v1.0 (by u/s3nl)")
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Purr~ Reddit Cat System Online.")

    @commands.command()
    async def cat(self, ctx: commands.Context):
        subreddit = await self.reddit.subreddit("cats")
        posts_list = []
        async for post in subreddit.new(limit=40):
            if post.author is not None and any(post.url.endswith(ext) for ext in [".png", ".jpg", ".jpeg", ".gif"]):
                author_name = post.author.name
                posts_list.append((post.url, author_name))
            if post.author is None:
                posts_list.append((post.url, "N/A"))

        if posts_list: 
            random_post = choice(posts_list)
            cat_embed = discord.Embed(title="Cat :cat:", description="KITTYYY :relaxed:", color=discord.Color.random())
            cat_embed.set_author(name=f":smiley_cat: PURRR A Cat Was Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
            cat_embed.set_image(url=random_post[0])
            cat_embed.set_footer(text=f"Purr~ :cat: This post was created by {random_post[1]}", icon_url=None)
            await ctx.send(embed=cat_embed)
        else:
            await ctx.send("Purr~ I was Unable to get cat :pensive:")
        if subreddit:
            await self.reddit.subreddit("cats")
        else:
            subreddit.close()


def cog_unload(self):
 self.bot.loop.create_task(self.reddit.close())
async def setup(bot):
   await bot.add_cog(redditcats(bot))