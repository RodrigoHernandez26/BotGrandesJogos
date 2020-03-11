import discord
from discord.ext import commands
from embeds import criar_var, var_fail, var_final, var_doisvotos, var_autor, var_cancelado
from utility import capitalizacao, hora, json, organizar

class Var(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def var(self, ctx, nome, ponto, *, msg):

        self.nome = capitalizacao(nome)
        self.ponto = int(ponto)
        self.msg = msg
        self.autor = ctx.author.name

        global var_on
        if not var_on:

            self.msg_bot = await ctx.send(embed = criar_var(msg, self.autor, self.nome, self.ponto))
            print(f'{hora()} - {ctx.author.name} criou um var.')

            await self.msg_bot.add_reaction('✅')
            await self.msg_bot.add_reaction('❌')

            var_on = True

        else:

            await ctx.send(embed = var_fail())
            print(f'{hora()} - {self.autor} tentou criar um novo var, mas já existe uma votação em andamento.')

    @commands.command()
    async def cancelarvar(self, ctx):
        global var_on
        
        with open('var.json', 'r') as f:
            var = json.load(f)

        if var_on:
            if ctx.author.name == self.autor:

                var_on = False

                var = {'Nomes':[], 'Votos': []}

                self.msg_bot.id = None

                self.num_n = 0
                self.num_p = 0

                with open('var.json', 'w') as f:
                    json.dump(var, f, indent= 4)

                await ctx.send(embed = var_cancelado())
                print(f'{hora()} - {ctx.author.name} cancelou o var.')
            
            else:
                ctx.send(embed = var_autor())
                print(f'{hora()} - {ctx.author.name} tentou cancelar uma var que não era seu.')

        else:
            await ctx.send(embed = var_fail())
            print(f'{hora()} - {ctx.author.name} tentou cancelar um var que não existe.')

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        global var_on
        self.num_p = 0
        self.num_n = 0

        with open('var.json', 'r') as f:
            var = json.load(f)

        if self.msg_bot.id == reaction.message.id and not user.name in var['Nomes'] and user.name != self.msg_bot.author.name:
            print(self.msg_bot.author.name)
            if reaction.emoji == '\u2705':
                var['Nomes'].append(user.name)
                var['Votos'].append(reaction.emoji)

                with open('var.json', 'w') as f:
                    json.dump(var, f, indent= 4)

                await self.msg_bot.edit(embed = criar_var(self.msg, self.autor, self.nome, self.ponto))
                print(f'{hora()} - {user.name} votou {reaction.emoji} no var.')
                self.num_p = reaction.count - 1

            elif reaction.emoji == '\u274c':
                var['Nomes'].append(user.name)
                var['Votos'].append(reaction.emoji)

                with open('var.json', 'w') as f:
                    json.dump(var, f, indent= 4)

                await self.msg_bot.edit(embed = criar_var(self.msg, self.autor, self.nome, self.ponto))
                print(f'{hora()} - {user.name} votou {reaction.emoji} no var.')
                self.num_n = reaction.count - 1

        elif user.name in var['Nomes']:

            await self.msg_bot.channel.send(embed = var_doisvotos(self.autor))
            print(f'{hora()} - {user.name} tentou votar duas vezes.')

        if self.num_p == 5 or self.num_n == 5:

            await self.msg_bot.delete()

            if self.num_p == 5:
                resultado = 'Confirmado!'
            else:
                resultado = 'Anulado!'

            await self.msg_bot.channel.send(embed = var_final(self.msg, self.autor, resultado))
            print(f'{hora()} - A votação foi encerrada, o resultado foi: {resultado}')

            with open('pontos.json', 'r') as p:
                pontos = json.load(p)

            for i in range(len(pontos['Nomes'])):
                if self.nome == pontos['Nomes'][i]:
                    x = i

            pontos['Pontos'] = pontos['Pontos'][x] + self.ponto

            with open('pontos.json', 'w') as p:
                json.dump(pontos, p, indent= 4)

            organizar()

            var_on = False

            var = {'Nomes':[], 'Votos': []}

            self.msg_bot.id = None

            self.num_n = 0
            self.num_p = 0

            with open('var.json', 'w') as f:
                json.dump(var, f, indent= 4)

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):

        with open('var.json', 'r') as f:
            var = json.load(f)

        for i in range(len(var['Nomes'])):
            if user.name == var['Nomes'][i]:
                x = i

        if reaction.emoji == var['Votos'][x]:

            if user.name in var['Nomes']:

                print(hora() + ' - ' + user.name + ' retirou seu voto: ' + var['Votos'][x])
                
                var['Nomes'].pop(x)
                var['Votos'].pop(x)

                with open('var.json', 'w') as f:
                    json.dump(var, f, indent= 4)
                
                await self.msg_bot.edit(embed = criar_var(self.msg, self.autor, self.nome, self.ponto))

def setup(client):
    client.add_cog(Var(client))
    global var_on
    var_on = False