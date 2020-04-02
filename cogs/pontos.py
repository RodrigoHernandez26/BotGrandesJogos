import discord
from discord.ext import commands
import yaml
from settings.utility import json, pontos_vazio, pontos_lista

class Pontos(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pontos(self, ctx):

        with open('settings/data.json', 'r') as f: data = json.load(f)
        with open('settings/settings.yaml', 'r') as f: settings = yaml.load(f, Loader= yaml.FullLoader)

        if ctx.channel.id != settings['CHAT_PNTS']:
            return

        if len(data['pnts']) == 0:
            await ctx.channel.send(embed = pontos_vazio())
        else:
            await ctx.channel.send(embed = pontos_lista())
   
def setup(client):
    client.add_cog(Pontos(client))