import discord
from discord.ext import commands
from settings.embeds import remover_nome, erro
from settings.db_commands import mysql_command

class Remover(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def remover(self, ctx, msg):

        nome = msg.lower().capitalize()

        data = mysql_command(f"select * from pnts where nome = '{nome}'", True)

        if len(data) != 0:
            mysql_command(f"delete from pnts where id_pontos = {data[0]['id_pontos']}")

            await ctx.channel.send(embed = remover_nome(nome))
            return
        
        await ctx.channel.send(embed = erro(nome))

def setup(client):
    client.add_cog(Remover(client))
