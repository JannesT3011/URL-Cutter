import discord
from discord import app_commands
from discord.ext import commands
import requests
from config import KEY  

class New(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
      self.bot = bot

    @commands.cooldown(1, 60.0, commands.BucketType.user)
    @app_commands.command(name="new", description="Cut a link")
    async def new(self, interaction: discord.Interaction, url:str) -> None: # TODO zu db hinzufügen: Usersdb:
        r = requests.get('http://cutt.ly/api/api.php?key={}&short={}'.format(KEY, url))
        data = r.json()["url"]
        embed = discord.Embed(title=f"New link", url=data["shortLink"])
        embed.add_field(name="Title:", value=data["title"], inline=False)
        embed.add_field(name="Full link:", value=data["fullLink"], inline=False)
        embed.add_field(name="Short link:", value=data["shortLink"], inline=False)
        embed.add_field(name="Date", value=data["date"], inline=False)

        return await interaction.response.send_message(embed=embed, ephemeral=True)

    @commands.cooldown(1, 60.0, commands.BucketType.user)
    @app_commands.command(name="stats", description="Show some stats about the link")
    async def stats(self, interaction: discord.Interaction, url:str) -> None:
        r = requests.get('http://cutt.ly/api/api.php?key={}&stats={}'.format(KEY, url))
        data = r.json()["stats"]
        embed = discord.Embed(title=f"Stats for `{data['title']}`")
        embed.add_field(name="Title:", value=data["title"], inline=False)
        embed.add_field(name="Full link:", value=data["fullLink"], inline=False)
        embed.add_field(name="Short link:", value=data["shortLink"], inline=False)
        embed.add_field(name="Date", value=data["date"], inline=False)
        embed.add_field(name="Clicks:", value=data["clicks"], inline=False)
        embed.add_field(name="Facebook:", value=data["facebook"], inline=False)
        embed.add_field(name="Twitter:", value=data["twitter"], inline=False)
        embed.add_field(name="Pinterest:", value=data["pinterest"], inline=False)
        embed.add_field(name="Instagram:", value=data["instagram"], inline=False)
        embed.add_field(name="googlePlus:", value=data["googlePlus"], inline=False)
        embed.add_field(name="Linkedin:", value=data["linkedin"], inline=False)
        embed.add_field(name="Rest:", value=data["rest"], inline=False)

        return await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="mylinks")
    async def mylinks(self, interaction:discord.Interaction) -> None:
      """RETURNS YOUR CREATED LINKS"""
      return
    



async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(New(bot))