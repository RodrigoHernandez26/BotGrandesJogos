import discord
from discord.ext import commands
import asyncio
import yaml
from settings.embeds import add_erro, add_singular, add_plural, add_limite
from settings.db_commands import mysql_command

class Add(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def add(self, ctx, ponto, nome):

        with open('settings/settings.yaml', 'r') as f: settings = yaml.load(f, Loader= yaml.FullLoader)

        nome = nome.lower().capitalize()

        try:
            int(ponto)
            assert int(ponto) > 0

            if int(ponto) > settings['LIM_ADD']: 
                await ctx.channel.send(embed = add_limite())
                return

        except Exception:
            await ctx.channel.send(embed = add_erro(nome, ponto))
            return

        data = mysql_command(f"select * from pnts where nome = '{nome}'", True)
        
        finalponto = int(data[0]['pontos']) + int(ponto)
        mysql_command(f"update pnts set pontos = {finalponto} where id_pontos = {data[0]['id_pontos']}")

        if int(ponto) == 1:
            await ctx.channel.send(embed = add_singular(nome))
            return
            
        else:
            await ctx.channel.send(embed = add_plural(nome, ponto))
            return
            
        await ctx.channel.send(embed = add_erro(nome, ponto))

def setup(client):
    client.add_cog(Add(client))