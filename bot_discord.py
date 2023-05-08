import discord
from setup import start_bot, get_ds_data
from commands import *
discord_data = get_ds_data()
bot, tree = start_bot()

# Commands Here
@tree.command(name='test', guild=discord.Object(discord_data['server_id'])) # DELETE AFTER FINISH
async def self(interaction: discord.Interaction):
    await test.run(interaction)




if __name__ == '__main__':
    bot.run(discord_data['token'])