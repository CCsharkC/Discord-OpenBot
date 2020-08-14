import discord
from discord.ext import commands
import os
import json

def get_prefix(client, message):
    with open("prefixes.json", "r") as pref:
        prefixes = json.load(pref)

    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix = get_prefix)

@bot.event
async def on_ready():
    print("Bot ready")

@bot.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as pref:
        prefixes = json.load(pref)

    prefixes[str(guild.id)] = "os."

    with open("prefixes.json", "w") as pref:
        json.dump(prefixes, pref)

for file in os.listdir("./modules"):
    if file.endswith(".py"):
        bot.load_extension(f"modules.{file[:-3]}")

bot.run("#token")
