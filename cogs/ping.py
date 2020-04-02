import discord
from discord.ext import commands
import yaml

class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):

        with open('settings/settings.yaml', 'r') as f: settings = yaml.load(f, Loader= yaml.FullLoader)

        if ctx.channel.id != settings['CHAT_PNTS']:
            return

        ping_embed = discord.Embed(
            title = f'⌛️ {round(self.client.latency * 1000)} ms',
            color = 0x22a7f0
        )
        await ctx.send(embed = ping_embed)
    
def setup(client):
    client.add_cog(Ping(client))