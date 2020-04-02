import discord
from discord.ext import commands
import yaml
from settings.utility import capitalizacao, json, retirar_erro, retirar_singular, retirar_plural

class Retirar(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def retirar(self, ctx, ponto, nome):

        with open('settings/data.json', 'r') as f: data = json.load(f)
        with open('settings/settings.yaml', 'r') as f: settings = yaml.load(f, Loader= yaml.FullLoader)

        if ctx.channel.id != settings['CHAT_PNTS']:
            return

        canal_log = self.client.get_channel(settings['CHAT_LOG'])

        nome = capitalizacao(nome)

        try:
            int(ponto)

        except ValueError:
            await ctx.channel.send(embed = retirar_erro(nome, ponto))
            return  
        
        try:

            assert int(ponto) > 0

            verif = False
            for name in data['pnts']:
                if nome == name['nome']:
                    verif = True
                    assert name['ponto'] - int(ponto) >= 0
            
            if not verif:
                await ctx.channel.send(embed = retirar_erro(nome, ponto))
                return

        except AssertionError:

            await ctx.channel.send(embed = retirar_erro(nome, ponto))
            return

        for name in data['pnts']:
            if nome == name['nome']:
                name['ponto'] -= int(ponto)
                finalponto = name['ponto']

        with open('settings/data.json', 'w') as f: json.dump(data, f, indent= 4)

        if int(ponto) == 1:

            await ctx.channel.send(embed = retirar_singular(nome))
            await canal_log.send(f'{ctx.author.name} retirou 1 ponto ao {nome}, ele tem {finalponto} agora.')
            
        else:

            await ctx.channel.send(embed = retirar_plural(nome, ponto))
            await canal_log.send(f'{ctx.author.name} retirou {ponto} pontos ao {nome}, ele tem {finalponto} agora.')
            
def setup(client):
    client.add_cog(Retirar(client))