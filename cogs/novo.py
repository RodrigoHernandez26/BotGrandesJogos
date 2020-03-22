import discord
from discord.ext import commands
from utility import capitalizacao, json, novo_repetido, novo_adicionado

class Novo(commands.Cog):

    def __init__(self, client):
        self.client = client       

    @commands.command()
    async def novo(self, ctx, msg):

        with open('data.json', 'r') as f: pontos = json.load(f)

        with open('data.json', 'r') as l: log = json.load(l)
        canal_log = self.client.get_channel(log['log'])
  
        nome = capitalizacao(msg)

        if len(pontos) == 0:
            pontos['pnts'].append({'nome': nome, 'ponto': 0}) 
        
        else:
            for name in pontos['pnts']:
                if nome == name['nome']:
                    await ctx.channel.send(embed = novo_repetido(nome))
                    return

            pontos['pnts'].append({'nome': nome, 'ponto': 0})

            with open('data.json', 'w') as f: json.dump(pontos, f, indent=4)

            await ctx.channel.send(embed = novo_adicionado(nome))
            await canal_log.send(f'{ctx.author.name} adicionou o {nome} ao jogo.')

def setup(client):
    client.add_cog(Novo(client))