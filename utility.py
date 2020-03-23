import discord
import json
from datetime import datetime

def capitalizacao(msg):
    return msg.lower().capitalize()

def organizar():

    with open('data.json', 'r') as f:
        pontos = json.load(f)

    for name in pontos['pnts']:
        for name2 in pontos['pnts']:
            if name['ponto'] > name2['ponto']:

                a = name['ponto']
                b = name['nome']

                name['ponto'] = name2['ponto']
                name['nome'] = name2['nome']

                name2['ponto'] = a
                name2['nome'] = b

    with open('pontos.json', 'w') as f:
        json.dump(pontos, f, indent= 4)

#**************************************************************************************************************#
#Embeds pontos.py

def pontos_vazio():
    embed = discord.Embed(
        title = 'Não há ninguém no jogo!',
        color = 0x22a7f0
    )
    embed.set_footer(text = '?help para ajuda')

    return embed
    
#*************************************************#
def pontos_lista():
    organizar()

    with open('pontos.json', 'r') as f: pontos = json.load(f)

    embed = discord.Embed(
        title = 'Os pontos são: ',
        color = 0x22a7f0
    )
    embed.set_footer(text= '?help para ajuda')

    cont = 0
    for nomes in pontos['pnts']:

        if cont == 0:
            embed.add_field(name = nomes['nome'] + '🥇', value = str(nomes['ponto']), inline = True)
        
        elif cont == 1:
            embed.add_field(name = nomes['nome'] + '🥈', value = str(nomes['ponto']), inline = True)

        elif cont == 2:
            embed.add_field(name = nomes['nome'] + '🥉', value = str(nomes['ponto']), inline = True)

        else:
            embed.add_field(name = nomes['nome'], value = str(nomes['ponto']), inline = True)
        cont += 1  

    return embed

#**************************************************************************************************************#
#Embeds novo.py

def novo_repetido(nome):
    embed = discord.Embed(
        title = f'O nome {nome} já foi adicionado ao jogo.',
        color = 0x22a7f0
    )
    embed.set_footer(text = '?help para ajuda')

    return embed

#*************************************************#

def novo_adicionado(nome):
    embed = discord.Embed(
        title = f'O nome {nome} foi adicionado ao jogo!',
        color = 0x22a7f0
    )
    embed.set_footer(text = '?help para ajuda')

    return embed

#**************************************************************************************************************#
#Embds remover.py

def remover_nome(nome):
    embed = discord.Embed(
        title = f'O nome {nome} foi retirado do jogo!',
        color = 0x22a7f0
    )
    embed.set_footer(text = '?help para ajuda')

    return embed

#**************************************************************************************************************#
#Embeds add.py

def add_erro(nome, ponto):
    embed = discord.Embed(
        title = 'Verifique se os parametros que foram passados estão corretos!',
        color = 0x22a7f0
    )
    embed.add_field(name = 'O nome passado foi:', value = nome, inline= False)
    embed.add_field(name = 'A quantidade de pontos a serem adicionado foi:', value = ponto, inline= False)
    embed.set_footer(text = '?help para ajuda')


    return embed

#*************************************************#

def add_singular(nome):
    embed = discord.Embed(
        title = f'Foi adicionado 1 ponto ao {nome}!',
        color = 0x22a7f0
    )
    embed.set_footer(text = '?help para ajuda')

    return embed

#*************************************************#

def add_plural(nome, ponto):
    embed = discord.Embed(
        title = f'Foi adicionado {ponto} pontos ao {nome}!',
        color = 0x22a7f0
    )

    embed.set_footer(text = '?help para ajuda')

    return embed

#**************************************************************************************************************#
#Embeds retirar.py

def retirar_erro(nome, ponto):
    embed = discord.Embed(
        title = 'Verifique se os parametros que foram passados estão corretos!',
        color = 0x22a7f0
    )
    embed.add_field(name = 'O nome passado foi:', value = nome, inline= False)
    embed.add_field(name = 'A quantidade de pontos a serem retirados foi:', value = ponto, inline= False)
    embed.add_field(name = f'Verifique se {nome} já não tem 0 pontos', value = f'Ou se retirar {ponto} ponto(s) vai deixa-lo com pontos negativos.', inline= False)
    embed.set_footer(text = '?help para ajuda')

    return embed

#*************************************************#

def retirar_singular(nome):
    embed = discord.Embed(
        title = f'Foi retirado 1 ponto do {nome}!',
        color = 0x22a7f0    
    )
    embed.set_footer(text = '?help para ajuda')

    return embed

#*************************************************#

def retirar_plural(nome, ponto):
    embed = discord.Embed(
        title = f'Foi retirado {ponto} pontos do {nome}!',
        color = 0x22a7f0
    )
    embed.set_footer(text = '?help para ajuda')

    return embed

#**************************************************************************************************************#
#Embed reset.py

def reset_true():
    embed = discord.Embed(
        title = 'Os nomes e pontos foram limpos!',
        color = 0x22a7f0
    )

    return embed

#*************************************************#

def reset_false():
    embed = discord.Embed(
        title = 'Você não tem permissão de usar esse comando',
        color = 0x22a7f0
    )

    return embed

#*************************************************#

def reset_fail():
    embed = discord.Embed(
        title = 'Não há ninguém no jogo!',
        color = 0x22a7f0
    )

    return embed

#**************************************************************************************************************#
#Embeds var

def criar_var(motivo, autor, nome, ponto):

    with open('data.json', 'r') as f: var = json.load(f)

    embed = discord.Embed(
        title = 'Nova votação criada:',
        color = 0x22a7f0
    )
    embed.set_footer(text = '?help para ajuda')
    embed.add_field(name = autor + ' criou a votação', value = motivo, inline=False)

    if ponto == 1:
        embed.add_field(name = 'Esse var vale:', value = f'{ponto} ponto para o {nome}', inline=False)
    else:
        embed.add_field(name = 'Esse var vale:', value = f'{ponto} pontos para o {nome}', inline=False)

    for name in var['var']:
        embed.add_field(name = name['nome'], value = name['voto'], inline= False)

    embed.set_image(url = 'https://media.tenor.com/images/8d649d1b182b5dc7c0befe0682c5c3cb/tenor.gif')

    return embed

#*************************************************#

def var_fail():
    embed = discord.Embed(
        title = 'Já existe uma votação em andamento!',
        color = 0x22a7f0
    )
    embed.set_footer(text = '?help para ajuda')

    return embed

#*************************************************#

def var_final(motivo, autor, resultado, nome, ponto):

    with open('data.json', 'r') as f: var = json.load(f)

    embed = discord.Embed(
        title = 'Resultado do var:',
        color = 0x22a7f0                   
    )
    embed.set_footer(text = '?help para ajuda')
    embed.add_field(name = autor + ' criou a votação', value = motivo, inline=False)

    if ponto == 1:
        embed.add_field(name = 'Esse var vale:', value = f'{ponto} ponto para o {nome}', inline=False)
    else:
        embed.add_field(name = 'Esse var vale:', value = f'{ponto} pontos para o {nome}', inline=False)

    for name in var['var']:
        embed.add_field(name = name['nome'], value = name['voto'], inline = False)

    embed.add_field(name = '\nO resultado final é: ', value = resultado, inline= False)
    embed.set_image(url = 'https://media.tenor.com/images/bc8e6e9ec05bc9ca408e94297a5c07e4/tenor.gif')

    return embed

#*************************************************#

def var_autor():
    embed = discord.Embed(
        title = 'Não foi você que iniciou essa votação!',
        color = 0x22a7f0
    )
    embed.set_footer(text = '?help para ajuda')

    return embed

#*************************************************#

def var_cancelado():

    embed = discord.Embed(
        title = 'O var foi cancelado!',
        color = 0x22a7f0
    )
    embed.set_footer(text = '?help para ajuda')

    return embed

#*************************************************#

def var_erro():

    embed = discord.Embed(
        title = 'Não existe uma votação em andamento!',
        color = 0x22a7f0
    )
    embed.set_footer(text = '?help para ajuda')

    return embed

#**************************************************************************************************************#
#Embed help.py

def help_embed():

    embed = discord.Embed(
        title = 'Como usar todos os comandos: ',
        color = 0x22a7f0
    )

    embed.set_footer(text = 'Verifique como está escrito o nome da pessoa pelo comando ?pontos. Os comandos e os nomes não tem sensibilidade a capitalização.')
    embed.add_field(name = '?novo', value = 'Adiciona uma nova pessoa ao jogo.\nEx: ?novo NomeDaPessoa', inline = False)
    embed.add_field(name = '?pontos', value = 'Lista os pontos por participante.\nEx: ?pontos', inline = False)
    embed.add_field(name = '?remover', value = 'Remove uma pessoa do jogo e exclui sua pontuação.\nEx: ?remover NomeDaPessoa', inline = False)
    embed.add_field(name = '?add', value = 'Adiciona pontos a uma pessoa.\nEx: ?add pontos NomeDaPessoa', inline = False)
    embed.add_field(name = '?retirar', value = 'Retira pontos de uma pessoa.\nEx: ?retirar pontos NomeDaPessoa', inline = False)
    embed.add_field(name = '?var', value = 'Inicia uma votação. (Necessário 5 votos para anular ou confirmar um var.)\nEx: ?var ponto nome "motivo"\nEx2: ?var 99 Megamente falou 99 vezes que o modolo é gay', inline = False)
    embed.add_field(name = '?cancelarvar', value = 'Cancela o var que você criou. (Somente a pessoa que iniciou o var pode cancela-lo).\nEx: ?cancelarvar', inline = False)
    embed.add_field(name = '?ping', value = 'Visualiza a latência do Bot.\nEx: ?ping', inline= False)

    return embed

#**************************************************************************************************************#
#Embed log

def log_add(nome):
    embed = discord.Embed(
        title = f'O canal {nome} foi definido como o log do BotPontos!',
        color = 0x22a7f0
    )

    return embed

#*************************************************#

def reset_log(nome):
    embed = discord.Embed(
        title = f'O canal {nome} não é mais o log do BotPontos.',
        color = 0x22a7f0
    )

    return embed

#*************************************************#

def erro_log():

    embed = discord.Embed(
        title = 'Esse não é um canal de log!',
        color = 0x22a7f0
    )

    return embed

#**************************************************************************************************************#
#Embed de erro

def erro(nome):

    embed = discord.Embed(
        title = f'O {nome} não está no jogo!',
        color = 0x22a7f0
    )
    embed.set_footer(text = '?help para ajuda')
    embed.add_field(name = 'Dica:', value = 'Use o ?pontos pra verificar o nome dos participantes.', inline = False)

    return embed

#**************************************************************************************************************#