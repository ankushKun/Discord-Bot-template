import discord
from discord.ext import commands
from decouple import config

links_str="""
[Youtube](https://www.youtube.com/channel/UCq4FMXXgsbsZmw5A-Mr7zSA), [GitHub](https://GitHub.com/ATCtech), [Twitter](https://twitter.com/ATC_YT_2014), [Instagram](https://instagram.com/weebletkun), [Reddit](https://www.reddit.com/u/TECHIE6023), [Fiverr](https://fiverr.com/atctech)
"""

class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    async def help(self,ctx):
        try:
            prefix=config("PREFIX")
            h = discord.Embed(title='',description='Need Help?',color=0xFF0000)
            h.add_field(name='__ABOUT__',value=f"\nPrefix : **{prefix}**\nDeveloped by : ``weeblet~kun#1193``")
            h.add_field(name='__MUSIC__',value='play, pause, resume, stop, skip, queue, join, shuffle, disconnect, remove')
            h.add_field(name='__MISC__',value='avatar, stats')
            h.add_field(name='__MODERATION__',value='announce, dm, clear, ban, unban, kickout')
            h.add_field(name='__DEVELOPER LINKS__',value=links_str)
            await ctx.send(embed=h)
        except Exception as e:
            print(e)

def setup(bot):
    bot.add_cog(Help(bot))
    print('---> HELP LOADED')
