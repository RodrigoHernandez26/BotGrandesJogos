import discord
from discord.ext import commands
from utility import capitalizacao, json, remover_nome, erro

class Remover(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def remover(self, ctx, msg):
        
        with open('data.json', 'r') as f: pontos = json.load(f)

        with open('data.json', 'r') as l: log = json.load(l)
        canal_log = self.client.get_channel(log['log'])

        nome = capitalizacao(msg)

        verif = False
        for name in pontos['pnts']:
            if nome == name['nome']:
                verif = True

        if not verif:
            await ctx.channel.send(embed = erro(nome))
            return

        else:
            cont = 0
            for name in pontos['pnts']:
                cont += 1
                if name['nome'] == nome:
                    pontos['pnts'].pop(cont - 1)

            await ctx.channel.send(embed = remover_nome(nome))
            await canal_log.send(f'{ctx.author.name} retirou o {nome} do jogo.')     

            with open('data.json', 'w') as f: json.dump(pontos, f, indent=4)

def setup(client):
    client.add_cog(Remover(client))
