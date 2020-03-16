import discord
from discord.ext import commands
import asyncio
from utility import capitalizacao, hora, json, add_erro, add_singular, add_plural

class Add(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def add(self, ctx, ponto, nome):

        with open('data.json', 'r') as f: pontos = json.load(f)

        with open('data.json', 'r') as l: log = json.load(l)

        canal_log = self.client.get_channel(log['log'])

        nome = capitalizacao(nome)

        try:
            int(ponto)

        except ValueError:
            await canal_log.send(f'{hora()} - {ctx.author.name} passou parametros errados.')
            await ctx.channel.send(embed = add_erro(nome, ponto))
            return

        try:
            assert int(ponto) > 0

            if int(ponto) > 100:
                msg_troll = await ctx.channel.send('Para de trolar ae corno')
                await asyncio.sleep(2)
                await msg_troll.delete()
                return

            verif = False
            for name in pontos['pnts']:
                if nome == name['nome']:
                    verif = True
            
            if not verif:
                await ctx.channel.send(embed = add_erro(nome, ponto))
                await canal_log.send(f'{hora()} - {ctx.author.name} passou parametros errados.')
                return

        except AssertionError:

            await ctx.channel.send(embed = add_erro(nome, ponto))
            await canal_log.send(f'{hora()} - {ctx.author.name} passou parametros errados.')
            return

        for name in pontos['pnts']:
            if nome == name['nome']:
                name['ponto'] += int(ponto)
                finalponto = name['ponto']

        with open('data.json', 'w') as f: json.dump(pontos, f, indent= 4)

        if int(ponto) == 1:

            await ctx.channel.send(embed = add_singular(nome))
            await canal_log.send(f'{hora()} - {ctx.author.name} adicinou 1 ponto ao {nome}, ele tem {finalponto} agora.')

        else:

            await ctx.channel.send(embed = add_plural(nome, ponto))
            await canal_log.send(f'{hora()} - {ctx.author.name} adicinou {ponto} pontos ao {nome}, ele tem {finalponto} agora.')

def setup(client):
    client.add_cog(Add(client))