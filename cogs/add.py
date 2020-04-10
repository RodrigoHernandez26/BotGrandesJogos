import discord
from discord.ext import commands
import asyncio
import yaml
from settings.embeds import add_erro, add_singular, add_plural
from settings.db_commands import mysql_command

class Add(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def add(self, ctx, ponto, nome):

        with open('settings/settings.yaml', 'r') as f: settings = yaml.load(f, Loader= yaml.FullLoader)

        if ctx.channel.id != settings['CHAT_PNTS']:
            return

        canal_log = self.client.get_channel(settings['CHAT_LOG'])

        nome = nome.lower().capitalize()

        try:
            int(ponto)
            assert int(ponto) > 0

            if int(ponto) > settings['LIM_ADD']: 
                msg_troll = await ctx.channel.send(settings['MSG_ADD'])
                await asyncio.sleep(2)
                await msg_troll.delete()
                return

        except Exception:
            await canal_log.send(f'{ctx.author.name} passou parametros errados.')
            await ctx.channel.send(embed = add_erro(nome, ponto))
            return

        data = mysql_command("select * from pnts", True)

        for i in range(len(data)):
            if data[i]['nome'] == nome:

                finalponto = int(data[i]['pontos']) + int(ponto)
                mysql_command(f"update pnts set pontos = {finalponto} where id_pontos = {data[i]['id_pontos']}")

                if int(ponto) == 1:
                    await ctx.channel.send(embed = add_singular(nome))
                    await canal_log.send(f'{ctx.author.name} adicinou 1 ponto ao {nome}, ele tem {finalponto} agora.')
                    return
                    
                else:
                    await ctx.channel.send(embed = add_plural(nome, ponto))
                    await canal_log.send(f'{ctx.author.name} adicinou {ponto} pontos ao {nome}, ele tem {finalponto} agora.')
                    return
            
        await canal_log.send(f'{ctx.author.name} passou parametros errados.')
        await ctx.channel.send(embed = add_erro(nome, ponto))

def setup(client):
    client.add_cog(Add(client))