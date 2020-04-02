import discord
from discord.ext import commands
import yaml
from settings.utility import capitalizacao, json, novo_repetido, novo_adicionado

class Novo(commands.Cog):

    def __init__(self, client):
        self.client = client       

    @commands.command()
    async def novo(self, ctx, msg):

        with open('settings/data.json', 'r') as f: data = json.load(f)
        with open('settings/settings.yaml', 'r') as f: settings = yaml.load(f, Loader= yaml.FullLoader)

        if ctx.channel.id != settings['CHAT_PNTS']:
            return

        canal_log = self.client.get_channel(settings['CHAT_LOG'])
  
        nome = capitalizacao(msg)

        if len(data) == 0:
            data['pnts'].append({'nome': nome, 'ponto': 0}) 
        
        else:
            for name in data['pnts']:
                if nome == name['nome']:
                    await ctx.channel.send(embed = novo_repetido(nome))
                    return

            data['pnts'].append({'nome': nome, 'ponto': 0})

            with open('settings/data.json', 'w') as f: json.dump(data, f, indent=4)

            await ctx.channel.send(embed = novo_adicionado(nome))
            await canal_log.send(f'{ctx.author.name} adicionou o {nome} ao jogo.')

def setup(client):
    client.add_cog(Novo(client))