import discord
import json
from discord.ext import commands
import os
import yaml

client = commands.Bot(command_prefix= '?', help_command= None)

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

with open('settings/settings.yaml', 'r') as f: data = yaml.load(f, Loader= yaml.FullLoader)
token = data['TOKEN_BOT']

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)