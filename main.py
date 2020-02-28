import discord
import asyncio
from datetime import datetime

bot = discord.Client()
lista_nomes = []
lista_pontos = []

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)
    print(datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))
    print('******** BOT ONLINE ********')
        
def capitalizacao(nome):
    return nome.lower().capitalize()

def hora():
    a = datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
    return (a)

def organizar(lista_nomes, lista_pontos):
    qnt_pontos = len(lista_pontos)
    for i in range (qnt_pontos):
        for j in range (qnt_pontos):
            if int(lista_pontos[i]) < int(lista_pontos[j]):
                a = lista_pontos[i]
                b = lista_nomes[i]
                lista_pontos[i] = lista_pontos[j]
                lista_nomes[i] = lista_nomes[j]
                lista_pontos[j] = a
                lista_nomes[j] = b
    lista_nomes.reverse()
    lista_pontos.reverse()

async def erro_nome(message):
    erro_embed = discord.Embed(
        title = 'Esse nome não está no jogo!',
        color = 0x22a7f0
    )
    erro_embed.set_footer(text = '?help para ajuda')
    erro_embed.add_field(name = 'Dica:', value = 'Use o ?pontos pra verificar o nome dos participantes.', inline = False)
    await message.channel.send(embed = erro_embed)

@bot.event
async def on_message(message):

    if message.content.lower().startswith('?novo'):
        nome = capitalizacao(message.content[6:])
        if nome in lista_nomes:
            novo_embedt = discord.Embed(
                title = 'O nome ' + nome + ' já foi adicionado ao jogo.',
                color = 0x22a7f0
            )
            novo_embedt.set_footer(text = '?help para ajuda')
            await message.channel.send(embed = novo_embedt)
            print(hora() + ' - O ' + message.author.name + ' tentou adicionar o ' + nome + ' novamente ao jogo.')
        else:
            lista_nomes.append(nome)
            lista_pontos.append('1')
            organizar(lista_nomes, lista_pontos)
            novo_embedf = discord.Embed(
                title = 'O nome ' + nome + ' foi adicionado ao jogo!',
                color = 0x22a7f0
            )
            novo_embedf.set_footer(text = '?help para ajuda')
            await message.channel.send(embed = novo_embedf)
            print(hora() + ' - O ' + message.author.name + ' adicionou o ' + nome + ' ao jogo.')
                 
    if message.content.lower().startswith('?pontos'):
        if len(lista_nomes) == 0:
            pnt_embedf = discord.Embed(
                title = 'Não há ninguém no jogo!',
                color = 0x22a7f0
            )
            pnt_embedf.set_footer(text = '?help para ajuda')
            await message.channel.send(embed = pnt_embedf)
            print(hora() + ' - O ' + message.author.name + ' solicitou a listagem dos pontos dos participantes do jogo, mas não tinha ninguém participando.')
        else:
            pnt_embed = discord.Embed(
                title = 'Os pontos são: ',
                color = 0x22a7f0
            )
            pnt_embed.set_footer(text = '?help para ajuda')
            for i in range(len(lista_nomes)):
                if i == 0:
                    pnt_embed.add_field(name = lista_nomes[i] + '🥇', value = lista_pontos[i], inline= True)
                elif i == 1:
                    pnt_embed.add_field(name = lista_nomes[i] + '🥈', value = lista_pontos[i], inline= True)
                elif i == 2:
                    pnt_embed.add_field(name = lista_nomes[i] + '🥉', value = lista_pontos[i], inline= True)
                else:
                    pnt_embed.add_field(name = lista_nomes[i], value = lista_pontos[i], inline= True)
            await message.channel.send(embed = pnt_embed)
            print(hora() + ' - O ' + message.author.name + ' solicitou a listagem dos pontos dos participantes do jogo.')

    if message.content.lower().startswith('?remover'):
        nome = capitalizacao(message.content[9:])
        verif = False
        try:
            pos = lista_nomes.index(nome)
            verif = True
        except ValueError:
            await erro_nome(message)
            print(hora() + ' - O ' + message.author.name + ' tentou tirar o nome ' + nome + ' do jogo, mas não tinha ninguém com esse nome.')
        if verif:
            lista_nomes.remove(nome)
            del(lista_pontos[pos])
            organizar(lista_nomes, lista_pontos)
            remover_embedt = discord.Embed(
                title = 'O nome ' + nome + ' foi retirado do jogo!',
                color = 0x22a7f0
            )
            remover_embedt.set_footer(text = '?help para ajuda')
            await message.channel.send(embed = remover_embedt)
            print(hora() + ' - O ' + message.author.name + ' retirou o ' + nome + ' do jogo.')

    if message.content.lower().startswith('?add'):
        numero = message.content[5:6]
        nome = capitalizacao(message.content[7:])
        if numero == '0':
            add_erro = discord.Embed(
                title = 'Não é possível adicionar 0 pontos!',
                color = 0x22a7f0
            )
            add_erro.set_footer(text = '?help para ajuda')
            await message.channel.send(embed = add_erro)
            print(hora() + ' - O ' + message.author.name + ' tentou adicionar 0 pontos do ' + nome + '.')
        else:
            verif = False
            try:
                pos = lista_nomes.index(nome)
                verif = True
            except ValueError:
                await erro_nome(message)
                if numero == 1:
                    print(hora() + ' - O ' + message.author.name + ' tentou adicionar 1 ponto ao ' + nome + ', mas não tinha ninguém com esse nome.')
                else:
                    print(hora() + ' - O ' + message.author.name + ' tentou adicionar ' + numero + ' pontos ao ' + nome + ', mas não tinha ninguém com esse nome.')
            if verif:
                conc = int(lista_pontos[pos])
                lista_pontos[pos] = conc + int(numero)
                organizar(lista_nomes, lista_pontos)
                addt_embeds = discord.Embed(
                    title = 'Foi adicionado 1 ponto ao ' + nome + '!',
                    color = 0x22a7f0
                )
                addt_embedp = discord.Embed(
                    title = 'Foi adicionado ' + numero + ' pontos ao ' + nome + '!',
                    color = 0x22a7f0
                )
                addt_embedp.set_footer(text = '?help para ajuda')
                addt_embeds.set_footer(text = '?help para ajuda')
                if numero == '1':
                    await message.channel.send(embed = addt_embeds)
                    print(hora() + ' - O ' + message.author.name + ' adicionou 1 ponto ao ' + nome + ', ele tem ' + str(lista_pontos[pos]) + ' agora.')
                else:
                    await message.channel.send(embed = addt_embedp)
                    print(hora() + ' - O ' + message.author.name + ' adicionou ' + numero + ' pontos ao ' + nome + ', ele tem ' + str(lista_pontos[pos]) + ' agora.')

    if message.content.lower().startswith('?retirar'):
        numero = message.content[9:10]
        nome = capitalizacao(message.content[11:])
        if numero == '0':
            retirar_erro = discord.Embed(
                title = 'Não é possível retirar 0 pontos!',
                color = 0x22a7f0
            )
            retirar_erro.set_footer(text = '?help para ajuda')
            await message.channel.send(embed = retirar_erro)
            print(hora() + ' - O ' + message.author.name + ' tentou retirar 0 pontos do ' + nome + '.')
        else:
            verif = False
            try:
                pos = lista_nomes.index(nome)
                verif = True
            except ValueError:
                await erro_nome(message)
                if numero == '1':
                    print(hora() + ' - O ' + message.author.name + ' tentou retirar 1 ponto ao ' + nome + ', mas não tinha ninguém com esse nome.')
                else:
                    print(hora() + ' - O ' + message.author.name + ' tentou retirar ' + numero + ' pontos ao ' + nome + ', mas não tinha ninguém com esse nome.')
            if verif:
                conc = int(lista_pontos[pos])
                if conc == 0:
                    retirar_erro = discord.Embed(
                        title = 'Essa pessoa já tem 0 pontos!',
                        color = 0x22a7f0
                    )
                    retirar_erro.set_footer(text = '?help para ajuda')
                    await message.channel.send(embed = retirar_erro)
                    if numero == '1':
                        print(hora() + ' - O ' + message.author.name + ' tentou retirar 1 ponto ao ' + nome + ', mas ele já tinha 0 pontos.')
                    else:
                        print(hora() + ' - O ' + message.author.name + ' tentou retirar ' + numero + ' pontos ao ' + nome + ', mas ele já tinha 0 pontos.')
                else:
                    lista_pontos[pos] = conc - int(numero)
                    organizar(lista_nomes, lista_pontos)
                    retirar_embeds = discord.Embed(
                        title = 'Foi retirado 1 ponto do ' + nome + '!',
                        color = 0x22a7f0
                    )
                    retirar_embedp = discord.Embed(
                        title = 'Foi retirado ' + numero + ' pontos do ' + nome + '!',
                        color = 0x22a7f0
                    )
                    retirar_embeds.set_footer(text = '?help para ajuda')
                    retirar_embedp.set_footer(text = '?help para ajuda')
                    if numero == '1':
                        await message.channel.send(embed = retirar_embeds)
                        print(hora() + ' - O ' + message.author.name + ' retirou 1 ponto ao ' + nome + ', ele tem ' + str(lista_pontos[pos]) + ' agora.')
                    else:
                        await message.channel.send(embed = retirar_embedp)
                        print(hora() + ' - O ' + message.author.name + ' retirou ' + numero + ' pontos ao ' + nome + ', ele tem ' + str(lista_pontos[pos]) + ' agora.')

    if message.content.lower().startswith('?help'):
        help_embed = discord.Embed(
            title = 'Como usar todos os comandos: ',
            color = 0x22a7f0
        )
        help_embed.set_footer(text = 'Verifique como está escrito o nome da pessoa pelo comando ?pontos. Os comandos não tem sensibilidade a capitalização.')
        help_embed.add_field(name = '?novo', value = 'Adiciona uma nova pessoa ao jogo (já é adicionado 1 ponto automaticamente.).\nEx: ?novo NomeDaPessoa', inline = False)
        help_embed.add_field(name = '?pontos', value = 'Lista os pontos por participante.\nEx: ?pontos', inline = False)
        help_embed.add_field(name = '?remover', value = 'Remove uma pessoa do jogo e exclui sua pontuação.\nEx: ?remover NomeDaPessoa', inline = False)
        help_embed.add_field(name = '?add', value = 'Adiciona pontos a uma pessoa.\nEx: ?add 1 NomeDaPessoa (1 - 9 pontos)', inline = False)
        help_embed.add_field(name = '?retirar', value = 'Retira pontos de uma pessoa.\nEx: ?retirar 1 NomeDaPessoa (1 - 9 pontos)', inline = False)
        await message.channel.send(embed = help_embed)
        print(hora() + ' - O ' + message.author.name + ' usou o ?help.')

    if message.content.lower().startswith('?reset'):
        if message.author.id == 232142342591741952:
            reset_embedt = discord.Embed(
                title = 'Os nomes e pontos foram limpos!',
                color = 0x22a7f0
            )
            await message.channel.send(embed = reset_embedt)
            print(hora() + ' - O ' + message.author.name + ' resetou o jogo.')
            print(lista_nomes)
            print(lista_pontos)
            lista_nomes.clear()
            lista_pontos.clear()
        else:
            reset_embedf = discord.Embed(
                title = 'Você não tem permissão de usar esse comando',
                color = 0x22a7f0
            )
            await message.channel.send(embed = reset_embedf)
            print(hora() + ' - O ' + message.author.name + ' tentou resetar o jogo.')
            
bot.run('Njc5MTUzNzU0MTc1NzAxMDMy.XllkjA.03YWg6le-yv4GhaFEzuiiKjwW-U')