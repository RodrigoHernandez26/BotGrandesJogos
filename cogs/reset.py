import discord
from discord.ext import commands
import yaml
from settings.embeds import reset_true, reset_false, reset_fail
from settings.db_commands import mysql_command

class Reset(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def reset(self, ctx):

        with open('settings/settings.yaml', 'r') as f: settings = yaml.load(f, Loader= yaml.FullLoader)

        if ctx.channel.id != settings['CHAT_PNTS']:
            return

        canal_log = self.client.get_channel(settings['CHAT_LOG'])

        data = mysql_command("select * from pnts", True)

        if len(data) != 0:
            if ctx.author.id == 232142342591741952:
                
                mysql_command("delete from pnts")

                await ctx.channel.send(embed = reset_true())
                await canal_log.send(f'{ctx.author.name} resetou o jogo.')

            else:

                await ctx.channel.send(embed = reset_false())
                await canal_log.send(f'{ctx.author.name} tentou resetar o jogo.')
            
        else:

            await ctx.channel.send(embed = reset_fail())
            await canal_log.send(f'{ctx.author.name} tentou resetar o jogo, mas não tinha ninguém participando.')


def setup(client):
    client.add_cog(Reset(client))