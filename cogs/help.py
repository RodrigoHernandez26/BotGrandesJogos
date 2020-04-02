import discord
from discord.ext import commands
import yaml
from settings.utility import help_embed

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):

        with open('settings/settings.yaml', 'r') as f: settings = yaml.load(f, Loader= yaml.FullLoader)

        if ctx.channel.id != settings['CHAT_PNTS']:
            return
            
        await ctx.send(embed = help_embed())

def setup(client):
    client.add_cog(Help(client))