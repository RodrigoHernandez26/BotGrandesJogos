import discord
from discord.ext import commands
import yaml
from settings.utility import capitalizacao, json, criar_var, var_fail, var_final, var_autor, var_cancelado, var_erro

class Var(commands.Cog):

    def __init__(self, client):
        self.client = client

        var_on = False
        self.var_on = var_on

        cheat_mode = False
        self.cheat_mode = cheat_mode
        
    @commands.command()
    async def var(self, ctx, ponto, nome, *, msg):

        with open('settings/settings.yaml', 'r') as f: settings = yaml.load(f, Loader= yaml.FullLoader)

        if ctx.channel.id != settings['CHAT_PNTS']:
            return
        
        canal_log = self.client.get_channel(settings['CHAT_LOG'])
        self.canal_log = canal_log

        self.nome = capitalizacao(nome)
        self.ponto = int(ponto)
        self.msg = msg
        self.autor = ctx.author.name

        if not self.var_on:

            self.msg_bot = await ctx.send(embed = criar_var(msg, self.autor, self.nome, self.ponto))
            await self.canal_log.send(f'{ctx.author.name} criou um var.')

            await self.msg_bot.add_reaction('✅')
            await self.msg_bot.add_reaction('❌')

            self.var_on = True

        else:
            await ctx.send(embed = var_fail())
            await self.canal_log.send(f'{self.autor} tentou criar um novo var, mas já existe uma votação em andamento.')

    @commands.command()
    async def cancelarvar(self, ctx):

        with open('settings/data.json', 'r') as f: data = json.load(f)
        with open('settings/settings.yaml', 'r') as f: settings = yaml.load(f, Loader= yaml.FullLoader)

        if ctx.channel.id != settings['CHAT_PNTS']:
            return

        self.canal_log = self.client.get_channel(settings['CHAT_LOG'])

        if self.var_on:
            if ctx.author.name == self.autor:

                self.var_on = False

                data['var'].clear()

                self.msg_bot.id = None

                self.num_n = 0
                self.num_p = 0

                with open('settings/data.json', 'w') as f: json.dump(data, f, indent= 4)

                await ctx.send(embed = var_cancelado())
                await self.canal_log.send(f'{ctx.author.name} cancelou o var.')
            
            else:
                ctx.send(embed = var_autor())
                await self.canal_log.send(f'{ctx.author.name} tentou cancelar uma var que não era seu.')

        else:
            await ctx.send(embed = var_erro())
            await self.canal_log.send(f'{ctx.author.name} tentou cancelar um var que não existe.')

    @commands.command()
    async def cheat(self, ctx):

        with open('settings/settings.yaml', 'r') as f: settings = yaml.load(f, Loader= yaml.FullLoader)

        if ctx.channel.id != settings['CHAT_PNTS']:
            return

        if self.cheat_mode:
            self.cheat_mode = False
        else:
            self.cheat_mode = True

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):

        with open('settings/data.json', 'r') as f: data = json.load(f)
        
        self.num_p = 0
        self.num_n = 0
        erro = False

        for name in data['var']:
            if name['nome'] == user.name:
                erro = True
        if self.msg_bot.id == reaction.message.id and not erro and user.name != self.msg_bot.author.name:
            if reaction.emoji == '\u2705':
                data['var'].append({'nome': user.name, 'voto': reaction.emoji})

                with open('settings/data.json', 'w') as f: json.dump(data, f, indent= 4)

                await self.msg_bot.edit(embed = criar_var(self.msg, self.autor, self.nome, self.ponto))
                await self.canal_log.send(f'{user.name} votou {reaction.emoji} no var.')
                self.num_p = reaction.count - 1

            elif reaction.emoji == '\u274c':
                data['var'].append({'nome': user.name, 'voto': reaction.emoji})

                with open('settings/data.json', 'w') as f: json.dump(data, f, indent= 4)

                await self.msg_bot.edit(embed = criar_var(self.msg, self.autor, self.nome, self.ponto))
                await self.canal_log.send(f'{user.name} votou {reaction.emoji} no var.')
                self.num_n = reaction.count - 1

        if (self.num_n == 5 or self.num_p == 5) or self.cheat_mode:

            await self.msg_bot.delete()

            if self.num_p == 5:
                resultado = 'Confirmado!'

                for name in data['pnts']:
                    if self.nome == name['nome']:

                        name['ponto'] += int(self.ponto)

                with open('settings/data.json', 'w') as p: json.dump(data, p, indent= 4)

            elif self.num_n == 5:
                resultado = 'Anulado!'
            
            else:
                resultado = 'Xitado!'

            await self.msg_bot.channel.send(embed = var_final(self.msg, self.autor, resultado, self.nome, self.ponto))
            await self.canal_log.send(f'A votação foi encerrada, o resultado foi: {resultado}')

            self.var_on = False

            data['var'].clear()

            self.msg_bot.id = None

            self.num_n = 0
            self.num_p = 0

            with open('settings/data.json', 'w') as f: json.dump(data, f, indent= 4)

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):

        with open('settings/data.json', 'r') as f: data = json.load(f)
        
        for name in data['var']:
            if user.name == name['nome']:
                reacao = name['voto']

        if reaction.emoji == reacao:

            cont = 0
            for name in data['var']:
                cont += 1
                if name['nome'] == user.name:
                    data['var'].pop(cont - 1)

                    await self.canal_log.send(f'{user.name} retirou seu voto: {reacao}')

                    with open('settings/data.json', 'w') as f: json.dump(data, f, indent= 4)
                    
                    await self.msg_bot.edit(embed = criar_var(self.msg, self.autor, self.nome, self.ponto))

def setup(client):
    client.add_cog(Var(client))