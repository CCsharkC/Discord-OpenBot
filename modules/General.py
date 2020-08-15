import discord
from discord.ext import commands
import json

class General(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """ping the bot and get latency back in chat"""
        await ctx.send(f"Pong: {round(self.bot.latency * 1000)}ms")

    @commands.command()
    async def discord(self, ctx):
        """sends the discord server link in chat"""
        await ctx.send("https://discord.gg/Hr8Fe9k")

    @commands.command()
    async def github(self, ctx):
        """sends the github link in chat"""
        await ctx.send("https://github.com/CCsharkC/Discord-OpenSBot")

    @commands.command()
    async def prefix(self, ctx, new_prefix):
            """changes the prefix for a server"""
            with open("prefixes.json", "r") as pref:
                prefixes = json.load(pref)

            prefixes[str(ctx.guild.id)] = new_prefix

            with open("prefixes.json", "w") as pref:
                json.dump(prefixes, pref)
            await ctx.send(f"Prefix Changed to {new_prefix}")
            
    @prefix.error
    async def prefix_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please provide a prefix")
        else:
            await ctx.send("Unexpected error, please try again")
            raise error


def setup(bot):
    bot.add_cog(General(bot))

