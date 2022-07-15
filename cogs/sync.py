import discord
from discord.ext import commands

class Sync(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def sync(self, ctx) -> None:
        await ctx.bot.tree.sync()
        return await ctx.reply("Synced!")

async def setup(bot):
    await bot.add_cog(Sync(bot))
