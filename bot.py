import discord
from discord.ext import commands
from config import TOKEN, KEY
from discord import utils

COGS = ["cogs.sync", "cogs.new"]

class Bot(commands.AutoShardedBot):
    def __init__(self, **kwargs):
        intents = discord.Intents.default()
        super(Bot, self).__init__(
            command_prefix=".",
            description="Chat with someone random!",
            intents=intents,
            #activity=discord.Activity(type=discord.ActivityType.watching, name=f"{PREFIX}help")
        )
        self.launch = __import__("datetime").datetime.utcnow()
        self.version = "v1.3.1"
        self.creator = "Bambus#8446"
        #self.ownerid = OWNERID
        #self.db = DbClient().collection
        #self.queuedb = DbClient().queuecollection
        #self.blacklist = self.load_blacklist()
        #
        #self.remove_command("bot")
        #self.remove_command("help")
    
    async def load_cogs(self):
        for ext in COGS:
            try:
                await self.load_extension(ext)
            except Exception as e:
                print(f"Cant load {ext}")
                raise e
    
        
    async def on_ready(self):
        await self.load_cogs()

        #data = {"server_count": len(self.guilds)}
        #requests.post(f"https://top.gg/api/bots/{self.user.id}/stats", headers={"Authorization": TOPGG_TOKEN}, data=data)
        print(f"{self.user.id}\n"f"{utils.oauth_url(self.user.id)}\n"f"{self.user.name}\n""Ready!")

bot = Bot()
bot.run(TOKEN)