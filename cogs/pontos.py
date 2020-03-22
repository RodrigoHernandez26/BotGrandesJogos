import discord
from discord.ext import commands
from utility import json, pontos_vazio, pontos_lista

class Pontos(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pontos(self, ctx):

        with open('data.json', 'r') as f: pontos = json.load(f)

        if len(pontos['pnts']) == 0:
            await ctx.channel.send(embed = pontos_vazio())
        else:
            await ctx.channel.send(embed = pontos_lista())
   
def setup(client):
    client.add_cog(Pontos(client))