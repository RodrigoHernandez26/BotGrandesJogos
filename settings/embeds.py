import discord
import json
from settings.db_commands import mysql_command

#0x22a7f0 - Azul (Status)
#0xff0000 - Vermelho (Erro)
#0x00ff00 - Verde (Sucesso)

#**************************************************************************************************************#
#Embeds pontos.py

def pontos_vazio():
    embed = discord.Embed(
        title = 'Não há ninguém no jogo!',
        color = 0xff0000
    )
    embed.set_footer(text = '?help para ajuda')

    return embed
    
#*************************************************#
def pontos_lista(data):

    embed = discord.Embed(
        title = 'Os pontos são: ',
        color = 0x22a7f0
    )
    embed.set_footer(text= '?help para ajuda')

    cont = 0
    for i in range(len(data)):

        if cont == 0:
            embed.add_field(name = data[i]['nome'] + '🥇', value = str(data[i]['pontos']), inline = True)
        
        elif cont == 1:
            embed.add_field(name = data[i]['nome'] + '🥈', value = str(data[i]['pontos']), inline = True)

        elif cont == 2:
            embed.add_field(name = data[i]['nome'] + '🥉', value = str(data[i]['pontos']), inline = True)

        else:
            embed.add_field(name = data[i]['nome'], value = str(data[i]['pontos']), inline = True)
        cont += 1  

    return embed

#**************************************************************************************************************#
#Embeds novo.py

def novo_repetido(nome):
    embed = discord.Embed(
        title = f'O nome {nome} já foi adicionado ao jogo.',
        color = 0xff0000
    )
    embed.set_footer(text = '?help para ajuda')

    return embed

#*************************************************#

def novo_adicionado(nome):
    embed = discord.Embed(
        title = f'O nome {nome} foi adicionado ao jogo!',
        color = 0x00ff00
    )
    embed.set_footer(text = '?help para ajuda')

    return embed

#**************************************************************************************************************#
#Embds remover.py

def remover_nome(nome):
    embed = discord.Embed(
        title = f'O nome {nome} foi retirado do jogo!',
        color = 0x00ff00
    )
    embed.set_footer(text = '?help para ajuda')

    return embed

#**************************************************************************************************************#
#Embeds add.py

def add_erro(nome, ponto):
    embed = discord.Embed(
        title = 'Verifique se os parametros que foram passados estão corretos!',
        color = 0xff0000
    )
    embed.add_field(name = 'O nome passado foi:', value = nome, inline= False)
    embed.add_field(name = 'A quantidade de pontos a serem adicionado foi:', value = ponto, inline= False)
    embed.set_footer(text = '?help para ajuda')


    return embed

#*************************************************#

def add_singular(nome):
    embed = discord.Embed(
        title = f'Foi adicionado 1 ponto ao {nome}!',
        color = 0x00ff00
    )
    embed.set_footer(text = '?help para ajuda')

    return embed

#*************************************************#

def add_plural(nome, ponto):
    embed = discord.Embed(
        title = f'Foi adicionado {ponto} pontos ao {nome}!',
        color = 0x00ff00
    )

    embed.set_footer(text = '?help para ajuda')

    return embed

#*************************************************#

def add_limite():
    embed = discord.Embed(
        title = 'Você não pode adicionar tantos pontos de uma vez',
        color = 0xff0000
    )
    embed.set_footer(text = '?help para ajuda')

    return embed

#**************************************************************************************************************#
#Embeds retirar.py

def retirar_erro(nome, ponto):
    embed = discord.Embed(
        title = 'Verifique se os parametros que foram passados estão corretos!',
        color = 0xff0000
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
        color = 0xff0000    
    )
    embed.set_footer(text = '?help para ajuda')

    return embed

#*************************************************#

def retirar_plural(nome, ponto):
    embed = discord.Embed(
        title = f'Foi retirado {ponto} pontos do {nome}!',
        color = 0xff0000
    )
    embed.set_footer(text = '?help para ajuda')

    return embed

#**************************************************************************************************************#
#Embed reset.py

def reset_true():
    embed = discord.Embed(
        title = 'Os nomes e pontos foram limpos!',
        color = 0x00ff00
    )
    embed.set_footer(text = '?help para ajuda')

    return embed

#*************************************************#

def reset_false():
    embed = discord.Embed(
        title = 'Você não tem permissão de usar esse comando',
        color = 0xff0000
    )
    embed.set_footer(text = '?help para ajuda')

    return embed

#*************************************************#

def reset_fail():
    embed = discord.Embed(
        title = 'Não há ninguém no jogo!',
        color = 0xff0000
    )
    embed.set_footer(text = '?help para ajuda')

    return embed

#*************************************************#

def reset_none():
    embed = discord.Embed(
        title = 'Defina um cargo para usar esse comando',
        color = 0x22a7f0
    )
    embed.set_footer(text = '?help para ajuda')

    return embed

#**************************************************************************************************************#
#Embeds var.py

def criar_var(votacao):

    embed = discord.Embed(
        title = 'Nova votação criada:',
        color = 0x22a7f0
    )
    embed.set_footer(text = '?help para ajuda')
    embed.add_field(name = votacao.autor + ' criou a votação', value = votacao.motivo, inline=False)

    if votacao.ponto == 1:
        embed.add_field(name = 'Esse var vale:', value = f'{votacao.ponto} ponto para o {votacao.alvo}', inline=False)
    else:
        embed.add_field(name = 'Esse var vale:', value = f'{votacao.ponto} pontos para o {votacao.alvo}', inline=False)

    for name in votacao.voto['votos']:
        embed.add_field(name = name['user'], value = name['voto'], inline= False)

    embed.set_image(url = 'https://media.tenor.com/images/8d649d1b182b5dc7c0befe0682c5c3cb/tenor.gif')

    return embed

#*************************************************#

def var_fail():
    embed = discord.Embed(
        title = 'Verifique se já existe uma votação ou se todos os argumentos do comando estão corretos.',
        color = 0xff0000
    )
    embed.set_footer(text = '?help para ajuda')

    return embed

#*************************************************#

def var_final(votacao, resultado):

    embed = discord.Embed(
        title = 'Resultado do var:',
        color = 0x22a7f0                   
    )
    embed.set_footer(text = '?help para ajuda')
    embed.add_field(name = votacao.autor + ' criou a votação', value = votacao.motivo, inline=False)

    if votacao.ponto == 1:
        embed.add_field(name = 'Esse var vale:', value = f'{votacao.ponto} ponto para o {votacao.alvo}', inline=False)
    else:
        embed.add_field(name = 'Esse var vale:', value = f'{votacao.ponto} pontos para o {votacao.alvo}', inline=False)

    for name in votacao.voto['votos']:
        embed.add_field(name = name['user'], value = name['voto'], inline = False)

    embed.add_field(name = '\nO resultado final é: ', value = resultado, inline= False)
    embed.set_image(url = 'https://media.tenor.com/images/bc8e6e9ec05bc9ca408e94297a5c07e4/tenor.gif')

    return embed

#*************************************************#

def var_autor():
    embed = discord.Embed(
        title = 'Não foi você que iniciou essa votação!',
        color = 0xff0000
    )
    embed.set_footer(text = '?help para ajuda')

    return embed

#*************************************************#

def var_cancelado():

    embed = discord.Embed(
        title = 'O var foi cancelado!',
        color = 0x00ff00
    )
    embed.set_footer(text = '?help para ajuda')

    return embed

#*************************************************#

def var_erro():

    embed = discord.Embed(
        title = 'Não existe uma votação em andamento!',
        color = 0xff0000
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
    embed.add_field(name = '?var', value = 'Inicia uma votação. (Necessário 5 votos para anular ou confirmar um var.)\nEx: ?var ponto nome "motivo"\nEx2: ?var 99 Megamente quebrou 99 vezes as regras', inline = False)
    embed.add_field(name = '?cancelarvar', value = 'Cancela o var que você criou. (Somente a pessoa que iniciou o var pode cancela-lo).\nEx: ?cancelarvar', inline = False)
    embed.add_field(name = '?ping', value = 'Visualiza a latência do Bot.\nEx: ?ping', inline= False)
    embed.add_field(name = 'Rolar Dados: ', value = 'dX - Rola 1 dado de X lado(s)\nEx: d10\n\nYdX - Rola Y dados de X lado(s)\nEX: 3d10\n\nZ#YdX - Rola Z vezes Y dados de X lado(s)\nEx: 5#3d10', inline= False)

    return embed

#**************************************************************************************************************#
#Embed setadm.py

def setadm_erro():
    embed = discord.Embed(
        title = 'ID de cargo inválido',
        color = 0xff0000
    )
    embed.set_footer(text = '?help para ajuda')

    return embed

#*************************************************#

def setadm_alterado(role):
    embed = discord.Embed(
        title = f'ADM alterado para o {role}',
        color = 0x00ff00
    )
    embed.set_footer(text = '?help para ajuda')

    return embed

#*************************************************#

def setadm_neg(dono):
    embed = discord.Embed(
        title = f'Somente o dono do servidor ({dono}) pode usar esse comando!',
        color = 0xff0000
    )
    embed.set_footer(text = '?help para ajuda')

    return embed

#**************************************************************************************************************#
#Embed de erro

def erro(nome):

    embed = discord.Embed(
        title = f'O {nome} não está no jogo!',
        color = 0xff0000
    )
    embed.set_footer(text = '?help para ajuda')
    embed.add_field(name = 'Dica:', value = 'Use o ?pontos pra verificar o nome dos participantes.', inline = False)

    return embed

#**************************************************************************************************************#