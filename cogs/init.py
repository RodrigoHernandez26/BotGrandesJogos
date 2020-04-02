import discord
from discord.ext import commands
from datetime import datetime

class Init(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game("?help para ajuda"))
        print(datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))
        print('** BOT ONLINE **')

def setup(client):
    client.add_cog(Init(client))