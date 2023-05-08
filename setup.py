import discord
from discord import app_commands
from config.settings import load_settings
from utils.load import read_yaml

settings = load_settings()
discord_data = read_yaml(settings['SECRETS'])
server_id = discord_data['server_id']



def start_bot():
    class MyBot(discord.Client):
        def __init__(self):
            super().__init__(intents=discord.Intents.default())
            self.synced = False

        async def on_ready(self):
            if not self.synced:
                await tree.sync(guild=discord.Object(id=discord_data['server_id']))
                self.synced = True
            print(f"Bot Online - {self.user}")

    bot = MyBot()
    tree = app_commands.CommandTree(bot)
    return bot, tree

def get_ds_data():
    return discord_data