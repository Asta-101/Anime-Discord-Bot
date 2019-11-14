import discord
from discord.ext import commands
import config
import os

bot = commands.Bot(command_prefix=".")


@bot.command()
@commands.has_permissions(administrator=True)
async def load(ctx,extension):
    bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"{extension} cog has been loaded!")

@bot.command()
@commands.has_permissions(administrator=True)
async def unload(ctx,extension):
    bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"{extension} cog has been unloaded")

@bot.command()
@commands.has_permissions(administrator=True)
async def reload(ctx,extension):
    bot.unload_extension(f"cogs.{extension}")
    bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"{extension} cog has been reloaded")

for filename in os.listdir("./cogs"):
    if filename.endswith("_cog.py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(config.TOKEN)