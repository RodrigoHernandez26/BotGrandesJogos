import discord
from discord.ext import commands
from utility import capitalizacao, hora, organizar, json
from embeds import retirar_erro, retirar_singular, retirar_plural, retirar_negativo, erro

class Retirar(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def retirar(self, ctx, ponto, nome):

        with open('pontos.json', 'r') as f:
            pontos = json.load(f)

        nome = capitalizacao(nome)

        if int(ponto) == 0:

            await ctx.channel.send(embed = retirar_erro())
            print(f'{hora()} - {ctx.author.name} tentou retirar 0 pontos do {nome}.')

        else:

            if nome in pontos['Nomes']:

                for i in range(len(pontos['Nomes'])):
                    if pontos['Nomes'][i] == nome:
                        x = i

                if pontos['Pontos'][x] - int(ponto) <= 0:

                    pontos['Pontos'][x] = pontos['Pontos'][x] - int(ponto)

                    with open('pontos.json', 'w') as f:
                        json.dump(pontos, f, indent= 4)

                    organizar()

                    if int(ponto) == 1:

                        await ctx.channel.send(embed = retirar_singular(nome))
                        print(hora() + ' - ' + ctx.author.name + ' retirou 1 ponto ao ' + nome + ', ele tem ' + str(pontos['Pontos'][x]) + ' agora.')
                    
                    else:

                        await ctx.channel.send(embed = retirar_plural(nome, ponto))
                        print(hora() + ' - ' + ctx.author.name + ' retirou ' + ponto + ' pontos ao ' + nome + ', ele tem ' + str(pontos['Pontos'][x]) + ' agora.')
                        

                else:
                    await ctx.send(embed = retirar_negativo(nome))
                    print(f'{hora()} - {ctx.author.name} tentou tirar {ponto} do {nome}, mas ele já tem 0 pontos')                 
           
            else:

                await ctx.channel.send(embed = erro(nome))

                if int(ponto) == 1:
                    print(f'{hora()} - {ctx.author.name} tentou retirar 1 ponto ao {nome}, mas não tinha ninguém com esse nome.')
                else:
                    print(f'{hora()} - {ctx.author.name} tentou retirar {ponto} pontos ao {nome}, mas não tinha ninguém com esse nome.')

def setup(client):
    client.add_cog(Retirar(client))