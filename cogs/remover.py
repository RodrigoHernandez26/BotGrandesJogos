import discord
from discord.ext import commands
import yaml
from settings.embeds import remover_nome, erro
from settings.db_commands import mysql_command

class Remover(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def remover(self, ctx, msg):

        with open('settings/settings.yaml', 'r') as f: settings = yaml.load(f, Loader= yaml.FullLoader)

        if ctx.channel.id != settings['CHAT_PNTS']:
            return

        canal_log = self.client.get_channel(settings['CHAT_LOG'])

        nome = msg.lower().capitalize()

        data = mysql_command("select * from pnts", True)

        for i in range(len(data)):
            if data[i]['nome'] == nome:
                mysql_command(f"delete from pnts where id_pontos = {data[i]['id_pontos']}")

                await ctx.channel.send(embed = remover_nome(nome))
                await canal_log.send(f'{ctx.author.name} retirou o {nome} do jogo.')
                return
        
        await ctx.channel.send(embed = erro(nome))

def setup(client):
    client.add_cog(Remover(client))
