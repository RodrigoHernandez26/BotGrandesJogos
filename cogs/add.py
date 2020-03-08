import discord
from discord.ext import commands
from utility import capitalizacao, hora, organizar, json
from embeds import add_zero, add_singular, add_plural, erro

class Add(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def add(self, ctx, ponto, nome):

        with open('pontos.json', 'r') as f:
            pontos = json.load(f)

        nome = capitalizacao(nome)

        if int(ponto) == 0:

            await ctx.channel.send(embed = add_zero())
            print(f'{hora()} - {ctx.author.name} tentou adicionar 0 pontos ao {nome}.')
            
        else:

            if nome in pontos['Nomes']:

                for i in range(len(pontos['Nomes'])):
                    if pontos['Nomes'][i] == nome:
                        x = i
                    
                pontos['Pontos'][x] = pontos['Pontos'][x] + int(ponto)

                with open('pontos.json', 'w') as f:
                    json.dump(pontos, f, indent= 4)

                organizar()

                if int(ponto) == 1:

                    await ctx.channel.send(embed = add_singular(nome))
                    print(hora() + ' - ' + ctx.author.name + ' adicionou 1 ponto ao ' + nome + ', ele tem ' + str(pontos['Pontos'][x]) + ' agora.')

                else:

                    await ctx.channel.send(embed = add_plural(nome, ponto))
                    print(hora() + ' - ' + ctx.author.name + ' adicionou ' + ponto + ' pontos ao ' + nome + ', ele tem ' + str(pontos['Pontos'][x]) + ' agora.')

            else:  

                await ctx.channel.send(embed = erro(nome))

                if int(ponto) == 1:
                    print(f'{hora()} - {ctx.author.name} tentou adicionar 1 ponto ao {nome}, mas não tinha ninguém com esse nome.')
                else:
                    print(f'{hora()} - {ctx.author.name} tentou adicionar {ponto} pontos ao {nome}, mas não tinha ninguém com esse nome.')


def setup(client):
    client.add_cog(Add(client))