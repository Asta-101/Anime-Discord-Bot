import discord
from discord.ext import commands


class Listeners(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged in as {self.bot.user}")
    

def setup(bot):
    bot.add_cog(Listeners(bot))