import discord
from discord.ext import commands
from utility import capitalizacao, hora, organizar, json
from embeds import novo_repetido, novo_adicionado

global data
data = {'Nomes':[], 'Pontos': []}

class Novo(commands.Cog):

    def __init__(self, client):
        self.client = client            

    @commands.command()
    async def novo(self, ctx, msg):
        global data

        with open('pontos.json', 'r') as f:
            pontos = json.load(f)
  
        nome = capitalizacao(msg)
        
        if (len(pontos) != 0):
            data = pontos

        if nome in pontos['Nomes']:

            await ctx.channel.send(embed = novo_repetido(nome))
            print(f'{hora()} - {ctx.author.name} tentou adicionar o {nome} novamente ao jogo.')
        
        else:
            data['Nomes'].append(nome)
            data['Pontos'].append(1)
            pontos = data

            await ctx.channel.send(embed = novo_adicionado(nome))
            print(f'{hora()} - {ctx.author.name} adicionou o {nome} ao jogo.')

        with open('pontos.json', 'w') as f:
            json.dump(pontos, f, indent=4)      
        
        organizar() 

def setup(client):
    client.add_cog(Novo(client))