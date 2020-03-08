import discord
from discord.ext import commands
from utility import hora, organizar, json
from embeds import pontos_vazio, pontos_lista

class Pontos(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pontos(self, ctx):

        organizar()

        with open('pontos.json', 'r') as f:
            pontos = json.load(f)

        if len(pontos['Nomes']) == 0:

            await ctx.channel.send(embed = pontos_vazio())
            print(f'{hora()} - {ctx.author.name} solicitou a listagem dos pontos dos participantes do jogo, mas não tinha ninguém participando.')

        else:

            await ctx.channel.send(embed = pontos_lista())
            print(f'{hora()} - {ctx.author.name} solicitou a listagem dos pontos dos participantes do jogo.')
   
def setup(client):
    client.add_cog(Pontos(client))