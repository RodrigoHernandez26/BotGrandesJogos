import discord
from discord.ext import commands
import yaml
from settings.utility import json, reset_true, reset_false, reset_fail

class Reset(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def reset(self, ctx):

        with open('settings/data.json', 'r') as f: data = json.load(f)
        with open('settings/settings.yaml', 'r') as f: settings = yaml.load(f, Loader= yaml.FullLoader)

        if ctx.channel.id != settings['CHAT_PNTS']:
            return

        canal_log = self.client.get_channel(settings['CHAT_LOG'])

        if len(data['pnts']) != 0:
            if ctx.author.id == 232142342591741952:
                
                data['pnts'].clear()

                with open('settings/data.json', 'w') as f: json.dump(data, f, indent= 4)

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