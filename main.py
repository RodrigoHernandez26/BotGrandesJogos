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
    log()

def log():
    log_nomes = open('log_nomes.txt', 'r')
    for i in log_nomes.readline().split():
        lista_nomes.append(i)
    print(lista_nomes)
    log_nomes.close()
    log_pontos = open('log_pontos.txt', 'r')
    for i in log_pontos.readline().split():
        lista_pontos.append(i)
    print(lista_pontos)
    log_pontos.close()

def capitalizacao(nome):
    return nome.lower().capitalize()

def hora():
    a = datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
    return (a)

def save(nome, ponto):
    log_nomes = open('log_nomes.txt', 'w')
    log_nomes.close()
    for i in range (len(nome)):
        write_nome(nome[i])
    log_nomes.close()
    log_pontos = open('log_pontos.txt', 'w')
    log_pontos.close()
    for j in range (len(ponto)):
        write_ponto(ponto[j])
    log_pontos.close()

def write_nome(nome):
    log_nomes = open('log_nomes.txt', 'a')
    log_nomes.write(' ' + nome)
    log_nomes.close()

def write_ponto(ponto):
    log_pontos = open('log_pontos.txt', 'a')
    log_pontos.write(' ' + str(ponto))
    log_pontos.close()

def write_log(mensagem):
    log = open('log.txt', 'a')
    log.write('%s\n' %mensagem)
    log.close()

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
    save(lista_nomes,lista_pontos)


@bot.event
async def on_message(message):

    if message.content.lower().startswith('?novo'):
        nome = capitalizacao(message.content[6:])
        print(nome)
        if nome in lista_nomes:
            await message.channel.send('O nome ' + nome + ' já foi adicionado ao jogo.')
            write_log(hora() + ' - O ' + message.author.name + ' tentou adicionar o ' + nome + ' novamente ao jogo.')
        else:
            lista_nomes.append(nome)
            lista_pontos.append('1')
            organizar(lista_nomes, lista_pontos)
            await message.channel.send('O nome ' + nome + ' foi adicionado ao jogo!')
            write_log(hora() + ' - O ' + message.author.name + ' adicionou o ' + nome + ' ao jogo.')
            print(lista_nomes)
                
    if message.content.lower().startswith('?nomes'):
        await message.channel.send('Os participantes do jogo são: ')
        for i in range (len(lista_nomes)):
            await message.channel.send(lista_nomes[i])
        write_log(hora() + ' - O ' + message.author.name + ' solicitou a listagem dos participantes do jogo.')

    if message.content.lower().startswith('?pontos'):
        print(lista_pontos)
        await message.channel.send('Os pontos são: ')
        for i in range (len(lista_nomes)):
            await message.channel.send(lista_nomes[i] + ': ' + str(lista_pontos[i]))
        write_log(hora() + ' - O ' + message.author.name + ' solicitou a listagem dos pontos dos participantes do jogo.')

    if message.content.lower().startswith('?remover'):
        nome = capitalizacao(message.content[9:])
        print(nome)
        pos = lista_nomes.index(nome)
        lista_nomes.remove(nome)
        del(lista_pontos[pos])
        organizar(lista_nomes, lista_pontos)
        await message.channel.send('O nome ' + nome + ' foi retirado do jogo!')
        write_log(hora() + ' - O ' + message.author.name + ' retirou o ' + nome + ' do jogo.')

    if message.content.lower().startswith('?add'):
        nome = capitalizacao(message.content[5:])
        print(nome)
        pos = lista_nomes.index(nome)
        conc = int(lista_pontos[pos])
        print(conc)
        lista_pontos[pos] = conc + 1
        organizar(lista_nomes, lista_pontos)
        await message.channel.send('Foi adicionado 1 ponto ao ' + nome + '!')
        write_log(hora() + ' - O ' + message.author.name + ' adicionou 1 ponto ao ' + nome + ', ele tem ' + str(lista_pontos[pos]) + ' agora.')

    if message.content.lower().startswith('?retirar'):
        nome = capitalizacao(message.content[9:])
        print(nome)
        pos = lista_nomes.index(nome)
        conc = int(lista_pontos[pos])
        print(conc)
        lista_pontos[pos] = conc - 1
        organizar(lista_nomes, lista_pontos)
        await message.channel.send('For retirado 1 ponto do ' + nome + '!')
        write_log(hora() + ' - O ' + message.author.name + ' retirou 1 ponto ao ' + nome + ', ele tem ' + str(lista_pontos[pos]) + ' agora.')

bot.run('Njc5MTUzNzU0MTc1NzAxMDMy.XktNSw.nY9_kDFHRlP3Bp36NT0X_CJ2J7Y')