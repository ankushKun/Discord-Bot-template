import discord
from discord.ext import commands
import os
from disputils import BotEmbedPaginator
import random



class Misc(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(aliases=["av","pfp"])
    async def avatar(self,ctx, mn:discord.User=None):
        if mn==None:
            mn=ctx.author
        p_emb = discord.Embed(title=" ", description="{}".format(mn.mention),color=0xFF0000)
        p_emb.set_image(url=mn.avatar_url)
        await ctx.send(embed=p_emb)

    @commands.command()
    async def stats(self,ctx):
        emb = discord.Embed(title="**STATS**",color=0xFF0000)
        emb.add_field(name="Total Servers",value=str(len(self.bot.guilds)),inline=False)
        emb.add_field(name="Latency(s)",value=str(round(self.bot.latency,3)),inline=False)
        emb.add_field(name=f"{ctx.guild} members",value=f'{ctx.guild.member_count}',inline=False)
        await ctx.send(embed=emb)


def setup(bot):
    bot.add_cog(Misc(bot))
    print('---> MISC LOADED')
