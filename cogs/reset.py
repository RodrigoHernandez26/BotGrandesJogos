import discord
from discord.ext import commands
from utility import json, reset_true, reset_false, reset_fail

class Reset(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def reset(self, ctx):

        with open('data.json', 'r') as f: pontos = json.load(f)

        with open('data.json', 'r') as l: log = json.load(l)
        canal_log = self.client.get_channel(log['log'])

        if len(pontos['pnts']) != 0:
            if ctx.author.id == 232142342591741952:
                
                pontos['pnts'].clear()

                with open('data.json', 'w') as f: json.dump(pontos, f, indent= 4)

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