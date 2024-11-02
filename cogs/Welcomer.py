import discord
from discord.ext import commands
import os
import easy_pil
import random

class welcomer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Purr~ Welcomer System Online")

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        welcome_channel = member.guild.system_channel
        images = [image for image in os.listdir("./cogs/welcomeassets")]
        randomized_image = random.choice(images)

        bg = easy_pil.Editor(f"./cogs/welcomeassets/{randomized_image}")
        avatar_image = await easy_pil.load_image_async(str(member.avatar.url))
        avatar = easy_pil.Editor(avatar_image).resize((250, 250)).circle_image()

        font_big = easy_pil.Font.poppins(size=90, variant="bold")
        font_small = easy_pil.Font.poppins(size=60, variant="bold")

        bg.paste(avatar, (835, 340))
        bg.ellipse((835, 340), 250, 250, outline="white", stroke_width=5)
        bg.text((960, 620), f"Purr~ Welcome to {member.guild.name}", color="white", font=font_big, align="center")
        bg.text((960, 740), f"Purr~ {member.name} is late to the party, bitch came in at number #{member.guild.member_count}.", color="white", font=font_small, align="center")

        img_File = discord.File(fp=bg.image_bytes, filename=randomized_image)
        await welcome_channel.send(f"BOOO, Did I scare you, {member.name}? Purr~")
        await welcome_channel.send(file=img_File)
async def setup(bot):
    await bot.add_cog(welcomer(bot))