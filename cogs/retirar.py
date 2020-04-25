import discord
from discord.ext import commands
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

        nome = nome.lower().capitalize()

        data = mysql_command(f"select * from pnts where nome = '{nome}' and server = {ctx.guild.id}", True)

        if len(data) != 0:

            if int(data[0]['pontos']) - int(ponto) >= 0:
                finalponto = int(data[0]['pontos']) - int(ponto)
                mysql_command(f"update pnts set pontos = {finalponto} where id_pontos = {data[0]['id_pontos']} and server = {ctx.guild.id}")

                if int(ponto) == 1:
                    await ctx.channel.send(embed = retirar_singular(nome))
                    return
                    
                else:
                    await ctx.channel.send(embed = retirar_plural(nome, ponto))
                    return

            else:
                await ctx.channel.send(embed = retirar_erro(nome, ponto))
                return
        
        await ctx.channel.send(embed = erro(nome))
   
def setup(client):
    client.add_cog(Retirar(client))