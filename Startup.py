import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "os.")

@bot.event
async def on_ready():
    print("Bot ready")

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong: {round(bot.latency * 1000)}ms")

bot.run("#token")
