import discord
from discord.ext import commands
import yaml
from settings.utility import capitalizacao, json, remover_nome, erro

class Remover(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def remover(self, ctx, msg):
        
        with open('settings/data.json', 'r') as f: data = json.load(f)
        with open('settings/settings.yaml', 'r') as f: settings = yaml.load(f, Loader= yaml.FullLoader)

        if ctx.channel.id != settings['CHAT_PNTS']:
            return

        canal_log = self.client.get_channel(settings['CHAT_LOG'])

        nome = capitalizacao(msg)

        verif = False
        for name in data['pnts']:
            if nome == name['nome']:
                verif = True

        if not verif:
            await ctx.channel.send(embed = erro(nome))
            return

        else:
            cont = 0
            for name in data['pnts']:
                cont += 1
                if name['nome'] == nome:
                    data['pnts'].pop(cont - 1)

            await ctx.channel.send(embed = remover_nome(nome))
            await canal_log.send(f'{ctx.author.name} retirou o {nome} do jogo.')     

            with open('settings/data.json', 'w') as f: json.dump(data, f, indent=4)

def setup(client):
    client.add_cog(Remover(client))
