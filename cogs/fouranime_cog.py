import discord
from discord.ext import commands
import aiohttp
from bs4 import BeautifulSoup as Soup 
from functions import fetch
from fourAnimeParser import Parser


class FourAnime(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot
        self.parser = Parser()
    @commands.command()
    async def watch(self,ctx,*,args):
        args = args.split(" ")
        try:
            episode_num = int(args[-1])
        except ValueError:
            await ctx.send("Invalid episode number!")
            return None

        name = '-'.join(args[:-1]).lower()

        fourAnimeLink = f"https://4anime.to/anime/{name}"

        info = await self.parser.getInfo(fourAnimeLink,episode_num)
        embed = discord.Embed(title=f"{info['title']} Episode {str(episode_num)}",colour=discord.Color.red())
        embed.set_thumbnail(url=info["image"])
        embed.add_field(name="Genres",value=info["genres"])
        embed.add_field(name="Link",value=info["episode"])

        await ctx.send(embed=embed)
        
        
        

def setup(bot):
    bot.add_cog(FourAnime(bot))