import discord
from discord.ext import commands
from settings.embeds import novo_repetido, novo_adicionado
from settings.db_commands import mysql_command

class Novo(commands.Cog):

    def __init__(self, client):
        self.client = client       

    @commands.command()
    async def novo(self, ctx, msg):

        nome = msg.lower().capitalize()

        data = mysql_command(f'select nome from pnts where nome = "{nome}"', True)
        if len(data) == 0:
            mysql_command(f'insert into pnts (nome) value ("{nome}")')

        else:
            await ctx.channel.send(embed = novo_repetido(nome))
            return

        await ctx.channel.send(embed = novo_adicionado(nome))

def setup(client):
    client.add_cog(Novo(client))