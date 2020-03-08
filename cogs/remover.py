import discord
from discord.ext import commands
from utility import capitalizacao, hora, organizar, json
from embeds import remover_nome, erro

class Remover(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def remover(self, ctx, msg):
        
        with open('pontos.json', 'r') as f:
            pontos = json.load(f)

        nome = capitalizacao(msg)

        if nome in pontos['Nomes']:

            for i in range(len(pontos['Nomes'])):
                if pontos['Nomes'][i] == nome:
                    x = i
                
            pontos['Nomes'].pop(x)
            pontos['Pontos'].pop(x)

            await ctx.channel.send(embed = remover_nome(nome))
            print(f'{hora()} - {ctx.author.name} retirou o {nome} do jogo.')     

            with open('pontos.json', 'w') as f:
                json.dump(pontos, f, indent=4)

            organizar()

        else:

            await ctx.channel.send(embed = erro(nome))
            print(f'{hora()} - {ctx.author.name} tentou tirar o nome {nome} do jogo, mas não tinha ninguém com esse nome.')


def setup(client):
    client.add_cog(Remover(client))
