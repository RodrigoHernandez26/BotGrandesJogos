import discord
from discord.ext import commands
from utility import hora

class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        ping_embed = discord.Embed(
            title = f'⌛️ {round(self.client.latency * 1000)} ms',
            color = 0x22a7f0
        )
        await ctx.send(embed = ping_embed)
        print(f'{hora()} - {ctx.author.name} pingou.')

    
def setup(client):
    client.add_cog(Ping(client))