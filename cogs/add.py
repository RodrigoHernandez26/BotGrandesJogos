import discord
from discord.ext import commands
import asyncio
import yaml
from settings.utility import capitalizacao, json, add_erro, add_singular, add_plural

class Add(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def add(self, ctx, ponto, nome):

        with open('settings/data.json', 'r') as f: data = json.load(f)
        with open('settings/settings.yaml', 'r') as f: settings = yaml.load(f, Loader= yaml.FullLoader)

        if ctx.channel.id != settings['CHAT_PNTS']:
            return

        canal_log = self.client.get_channel(settings['CHAT_LOG'])

        nome = capitalizacao(nome)

        try:
            int(ponto)

        except ValueError:
            await canal_log.send(f'{ctx.author.name} passou parametros errados.')
            await ctx.channel.send(embed = add_erro(nome, ponto))
            return

        try:
            assert int(ponto) > 0
            if int(ponto) > settings['LIM_ADD']: 
                msg_troll = await ctx.channel.send(settings['MSG_ADD'])
                await asyncio.sleep(2)
                await msg_troll.delete()
                return

            verif = False
            for name in data['pnts']:
                if nome == name['nome']:
                    verif = True
            
            if not verif:
                await ctx.channel.send(embed = add_erro(nome, ponto))
                await canal_log.send(f'{ctx.author.name} passou parametros errados.')
                return

        except AssertionError:

            await ctx.channel.send(embed = add_erro(nome, ponto))
            await canal_log.send(f'{ctx.author.name} passou parametros errados.')
            return

        for name in data['pnts']:
            if nome == name['nome']:
                name['ponto'] += int(ponto)
                finalponto = name['ponto']

        with open('settings/data.json', 'w') as f: json.dump(data, f, indent= 4)

        if int(ponto) == 1:

            await ctx.channel.send(embed = add_singular(nome))
            await canal_log.send(f'{ctx.author.name} adicinou 1 ponto ao {nome}, ele tem {finalponto} agora.')

        else:

            await ctx.channel.send(embed = add_plural(nome, ponto))
            await canal_log.send(f'{ctx.author.name} adicinou {ponto} pontos ao {nome}, ele tem {finalponto} agora.')

def setup(client):
    client.add_cog(Add(client))