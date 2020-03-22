import discord
import json
from discord.ext import commands
from utility import log_add, reset_log, erro_log

class Log(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def log(self, ctx):

        self.canal = ctx.channel.name
        self.id = ctx.channel.id
        
        with open('data.json', 'r') as f: log = json.load(f)

        log['log'] = ctx.channel.id

        with open('data.json', 'w') as f: json.dump(log, f, indent= 4)

        await ctx.send(embed = log_add(ctx.channel.name))
        print(f'Definido o canal {ctx.channel.name} como log (id:{ctx.channel.id})')

    @commands.command()
    async def resetlog(self, ctx):

        with open('data.json', 'r') as f: log = json.load(f)

        if ctx.channel.id == self.id and ctx.channel.name == self.canal and log['log'] != '':

            log['log'] = ''

            with open('data.json', 'w') as f: json.dump(log, f, indent= 4)

            await ctx.send(embed = reset_log(ctx.channel.name))
            print(f'Removeu o log do canal {ctx.channel.name} (id:{ctx.channel.id})')
        
        else:
            
            await ctx.send(embed = erro_log())
            print(f'Erro no reset log.')

def setup(client):
    client.add_cog(Log(client))