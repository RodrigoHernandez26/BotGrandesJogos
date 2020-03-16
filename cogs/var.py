import discord
from discord.ext import commands
from utility import capitalizacao, hora, json, criar_var, var_fail, var_final, var_doisvotos, var_autor, var_cancelado, var_erro

class Var(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def var(self, ctx, ponto, nome, *, msg):

        self.nome = capitalizacao(nome)
        self.ponto = int(ponto)
        self.msg = msg
        self.autor = ctx.author.name

        with open('data.json', 'r') as l: log = json.load(l)
        canal_log = self.client.get_channel(log['log'])

        global var_on
        if not var_on:

            self.msg_bot = await ctx.send(embed = criar_var(msg, self.autor, self.nome, self.ponto))
            await canal_log.send(f'{hora()} - {ctx.author.name} criou um var.')

            await self.msg_bot.add_reaction('✅')
            await self.msg_bot.add_reaction('❌')

            var_on = True

        else:
            await ctx.send(embed = var_fail())
            await canal_log.send(f'{hora()} - {self.autor} tentou criar um novo var, mas já existe uma votação em andamento.')

    @commands.command()
    async def cancelarvar(self, ctx):
        global var_on
        
        with open('data.json', 'r') as f: var = json.load(f)

        with open('data.json', 'r') as l: log = json.load(l)
        canal_log = self.client.get_channel(log['log'])

        if var_on:
            if ctx.author.name == self.autor:

                var_on = False

                var['var'].clear()

                self.msg_bot.id = None

                self.num_n = 0
                self.num_p = 0

                with open('data.json', 'w') as f: json.dump(var, f, indent= 4)

                await ctx.send(embed = var_cancelado())
                await canal_log.send(f'{hora()} - {ctx.author.name} cancelou o var.')
            
            else:
                ctx.send(embed = var_autor())
                await canal_log.send(f'{hora()} - {ctx.author.name} tentou cancelar uma var que não era seu.')

        else:
            await ctx.send(embed = var_erro())
            await canal_log.send(f'{hora()} - {ctx.author.name} tentou cancelar um var que não existe.')

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        global var_on
        self.num_p = 0
        self.num_n = 0
        erro = False

        with open('data.json', 'r') as f: var = json.load(f)

        with open('data.json', 'r') as l: log = json.load(l)
        canal_log = self.client.get_channel(log['log'])

        for name in var['var']:
            if name['nome'] == user.name:
                erro = True
        if self.msg_bot.id == reaction.message.id and not erro and user.name != self.msg_bot.author.name:
            if reaction.emoji == '\u2705':
                var['var'].append({'nome': user.name, 'voto': reaction.emoji})

                with open('data.json', 'w') as f: json.dump(var, f, indent= 4)

                await self.msg_bot.edit(embed = criar_var(self.msg, self.autor, self.nome, self.ponto))
                await canal_log.send(f'{hora()} - {user.name} votou {reaction.emoji} no var.')
                self.num_p = reaction.count - 1

            elif reaction.emoji == '\u274c':
                var['var'].append({'nome': user.name, 'voto': reaction.emoji})

                with open('data.json', 'w') as f: json.dump(var, f, indent= 4)

                await self.msg_bot.edit(embed = criar_var(self.msg, self.autor, self.nome, self.ponto))
                await canal_log.send(f'{hora()} - {user.name} votou {reaction.emoji} no var.')
                self.num_n = reaction.count - 1

        else:
            for name in var['var']:
                if user.name == name['nome']:
                    await self.msg_bot.channel.send(embed = var_doisvotos(user.name))
                    await canal_log.send(f'{hora()} - {user.name} tentou votar duas vezes.')

        if self.num_p == 5 or self.num_n == 5:

            await self.msg_bot.delete()

            if self.num_p == 5:
                resultado = 'Confirmado!'
                
                with open('data.json', 'r') as p: pontos = json.load(p)

                for name in pontos['pnts']:
                    if self.nome == name['nome']:
                        name['ponto'] += int(self.ponto)

                with open('pontos.json', 'w') as p: json.dump(pontos, p, indent= 4)

            else:
                resultado = 'Anulado!'

            await self.msg_bot.channel.send(embed = var_final(self.msg, self.autor, resultado, self.nome, self.ponto))
            await canal_log.send(f'{hora()} - A votação foi encerrada, o resultado foi: {resultado}')

            var_on = False

            var['var'].clear()

            self.msg_bot.id = None

            self.num_n = 0
            self.num_p = 0

            with open('var.json', 'w') as f: json.dump(var, f, indent= 4)

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):

        with open('data.json', 'r') as f: var = json.load(f)

        with open('data.json', 'r') as l: log = json.load(l)
        canal_log = self.client.get_channel(log['log'])
        
        for name in var['var']:
            if user.name == name['nome']:
                reacao = name['voto']

        if reaction.emoji == reacao:

            cont = 0
            for name in var['var']:
                cont += 1
                if name['nome'] == user.name:
                    var['var'].pop(cont - 1)

                    await canal_log.send(f'{hora()} - {user.name} retirou seu voto: {reacao}')

                    with open('data.json', 'w') as f: json.dump(var, f, indent= 4)
                    
                    await self.msg_bot.edit(embed = criar_var(self.msg, self.autor, self.nome, self.ponto))

def setup(client):
    client.add_cog(Var(client))
    global var_on
    var_on = False