import discord
from discord.ext import commands
from utility import hora, json
from embeds import reset_true, reset_false, reset_fail

class Reset(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def reset(self, ctx):

        with open('pontos.json', 'r') as f:
            pontos = json.load(f)

        if len(pontos['Nomes']) != 0:
            if ctx.author.id == 232142342591741952:
                
                pontos = {'Nomes':[], 'Pontos': []}

                with open('pontos.json', 'w') as f:
                    json.dump(pontos, f, indent= 4)

                await ctx.channel.send(embed = reset_true())
                print(f'{hora()} - {ctx.author.name} resetou o jogo.')

            else:

                await ctx.channel.send(embed = reset_false())
                print(f'{hora()} - {ctx.author.name} tentou resetar o jogo.')
            
        else:

            await ctx.channel.send(embed = reset_fail())
            print(f'{hora()} - {ctx.author.name} tentou resetar o jogo, mas não tinha ninguém participando.')


def setup(client):
    client.add_cog(Reset(client))