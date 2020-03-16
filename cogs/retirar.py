import discord
from discord.ext import commands
from utility import capitalizacao, hora, json, retirar_erro, retirar_singular, retirar_plural

class Retirar(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def retirar(self, ctx, ponto, nome):

        with open('data.json', 'r') as f: pontos = json.load(f)

        with open('data.json', 'r') as l: log = json.load(l)
        canal_log = self.client.get_channel(log['log'])

        nome = capitalizacao(nome)

        try:
            int(ponto)

        except ValueError:
            await ctx.channel.send(embed = retirar_erro(nome, ponto))
            await canal_log.send(f'{hora()} - {ctx.author.name} passou parametros errados.')
            return  
        
        try:

            assert int(ponto) > 0

            verif = False
            for name in pontos['pnts']:
                if nome == name['nome']:
                    verif = True
                    assert name['ponto'] - int(ponto) >= 0
            
            if not verif:
                await ctx.channel.send(embed = retirar_erro(nome, ponto))
                await canal_log.send(f'{hora()} - {ctx.author.name} passou parametros errados.')
                return

        except AssertionError:

            await ctx.channel.send(embed = retirar_erro(nome, ponto))
            await canal_log.send(f'{hora()} - {ctx.author.name} passou parametros errados.')
            return

        for name in pontos['pnts']:
            if nome == name['nome']:
                name['ponto'] -= int(ponto)
                finalponto = name['ponto']

        with open('data.json', 'w') as f: json.dump(pontos, f, indent= 4)

        if int(ponto) == 1:

            await ctx.channel.send(embed = retirar_singular(nome))
            await canal_log.send(f'{hora()} - {ctx.author.name} retirou 1 ponto ao {nome}, ele tem {finalponto} agora.')
            
        else:

            await ctx.channel.send(embed = retirar_plural(nome, ponto))
            await canal_log.send(f'{hora()} - {ctx.author.name} retirou {ponto} pontos ao {nome}, ele tem {finalponto} agora.')
            
def setup(client):
    client.add_cog(Retirar(client))