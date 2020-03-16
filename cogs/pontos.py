import discord
from discord.ext import commands
from utility import hora, json, pontos_vazio, pontos_lista

class Pontos(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pontos(self, ctx):

        with open('data.json', 'r') as f: pontos = json.load(f)

        with open('data.json', 'r') as l: log = json.load(l)
        canal_log = self.client.get_channel(log['log'])

        if len(pontos['pnts']) == 0:

            await ctx.channel.send(embed = pontos_vazio())
            await canal_log.send(f'{hora()} - {ctx.author.name} solicitou a listagem dos pontos dos participantes do jogo, mas não tinha ninguém participando.')

        else:

            await ctx.channel.send(embed = pontos_lista())
            await canal_log.send(f'{hora()} - {ctx.author.name} solicitou a listagem dos pontos dos participantes do jogo.')
   
def setup(client):
    client.add_cog(Pontos(client))