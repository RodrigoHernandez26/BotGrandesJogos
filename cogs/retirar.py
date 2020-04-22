import discord
from discord.ext import commands
import yaml
from settings.embeds import retirar_erro, retirar_singular, retirar_plural, erro
from settings.db_commands import mysql_command

class Retirar(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def retirar(self, ctx, ponto, nome):

        try:
            int(ponto)
            assert int(ponto) > 0
        
        except Exception:
            await ctx.channel.send(embed = retirar_erro(nome, ponto))
            return

        with open('settings/settings.yaml', 'r') as f: settings = yaml.load(f, Loader= yaml.FullLoader)

        if ctx.channel.id != settings['CHAT_PNTS']:
            return

        canal_log = self.client.get_channel(settings['CHAT_LOG'])

        nome = nome.lower().capitalize()

        data = mysql_command(f"select * from pnts where nome = '{nome}'", True)

        if len(data) != 0:

            if int(data[0]['pontos']) - int(ponto) >= 0:

                finalponto = int(data[0]['pontos']) - int(ponto)
                mysql_command(f"update pnts set pontos = {finalponto} where id_pontos = {data[0]['id_pontos']}")

                if int(ponto) == 1:

                    await ctx.channel.send(embed = retirar_singular(nome))
                    await canal_log.send(f'{ctx.author.name} retirou 1 ponto ao {nome}, ele tem {finalponto} agora.')
                    return
                    
                else:

                    await ctx.channel.send(embed = retirar_plural(nome, ponto))
                    await canal_log.send(f'{ctx.author.name} retirou {ponto} pontos ao {nome}, ele tem {finalponto} agora.')
                    return

            else:
                await ctx.channel.send(embed = retirar_erro(nome, ponto))
                return
        
        await ctx.channel.send(embed = erro(nome))
   
def setup(client):
    client.add_cog(Retirar(client))