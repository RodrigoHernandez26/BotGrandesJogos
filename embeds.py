import discord
import json

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

    with open('pontos.json', 'r') as f:
        pontos = json.load(f)

    embed = discord.Embed(
        title = 'Os pontos são: ',
        color = 0x22a7f0
    )
    embed.set_footer(text= '?help para ajuda') #verificar help!!!!!!!!!

    for i in range(len(pontos['Nomes'])):
        
        if i == 0:
            embed.add_field(name = pontos['Nomes'][i] + '🥇', value = pontos['Pontos'][i], inline = True)
        
        elif i == 1:
            embed.add_field(name = pontos['Nomes'][i] + '🥈', value = pontos['Pontos'][i], inline = True)

        elif i == 2:
            embed.add_field(name = pontos['Nomes'][i] + '🥉', value = pontos['Pontos'][i], inline = True)

        else:
            embed.add_field(name = pontos['Nomes'][i], value = pontos['Pontos'][i], inline = True)
            
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

def add_zero():
    embed = discord.Embed(
        title = 'Não é possível adicionar 0 pontos!',
        color = 0x22a7f0
    )
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

def retirar_erro():
    embed = discord.Embed(
        title = 'Não é possível retirar 0 pontos!',
        color = 0x22a7f0
    )
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

#*************************************************#

def retirar_negativo(nome):
    embed = discord.Embed(
        title = f'{nome} já tem 0 pontos.',
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

    with open('var.json', 'r') as f:
        var = json.load(f)

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

    for i in range(len(var['Nomes'])):
        embed.add_field(name = var['Nomes'][i], value = var['Votos'][i], inline= False)
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

    with open('var.json', 'r') as f:
        var = json.load(f)

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

    for i in range (len(var['Nomes'])):
        embed.add_field(name = var['Nomes'][i], value = var['Votos'][i], inline = False)

    embed.add_field(name = '\nO resultado final é: ', value = resultado, inline= False)
    embed.set_image(url = 'https://media.tenor.com/images/bc8e6e9ec05bc9ca408e94297a5c07e4/tenor.gif')

    return embed

#*************************************************#

def var_doisvotos(autor):

    with open('var.json', 'r') as f:
        var = json.load(f)

    for i in range (len(var['Nomes'])):
        if var['Nomes'][i] == autor:
            x = i

    embed = discord.Embed(
        title = 'Você já votou nesse var: ' + var['Nomes'][x] + ' --> ' + var['Votos'][x],
        color = 0x22a7f0 
    )
    embed.set_footer(text = '?help para ajuda')

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

#**************************************************************************************************************#
#Embed help.py

def help_embed():

    embed = discord.Embed(
        title = 'Como usar todos os comandos: ',
        color = 0x22a7f0
    )

    embed.set_footer(text = 'Verifique como está escrito o nome da pessoa pelo comando ?pontos. Os comandos e os nomes não tem sensibilidade a capitalização.')
    embed.add_field(name = '?novo', value = 'Adiciona uma nova pessoa ao jogo (já é adicionado 1 ponto automaticamente.).\nEx: ?novo NomeDaPessoa', inline = False)
    embed.add_field(name = '?pontos', value = 'Lista os pontos por participante.\nEx: ?pontos', inline = False)
    embed.add_field(name = '?remover', value = 'Remove uma pessoa do jogo e exclui sua pontuação.\nEx: ?remover NomeDaPessoa', inline = False)
    embed.add_field(name = '?add', value = 'Adiciona pontos a uma pessoa.\nEx: ?add pontos NomeDaPessoa', inline = False)
    embed.add_field(name = '?retirar', value = 'Retira pontos de uma pessoa.\nEx: ?retirar pontos NomeDaPessoa', inline = False)
    embed.add_field(name = '?var', value = 'Inicia uma votação. (Necessário 5 votos para anular ou confirmar um var.)\nEx: ?var nome pontos "motivo"\nEx2: ?var Megamente 99 falou 99 vezes que o modolo é gay', inline = False)
    embed.add_field(name = '?cancelarvar', value = 'Cancela o var que você criou. (Somente a pessoa que iniciou o var pode cancela-lo).\nEx: ?cancelarvar', inline = False)
    embed.add_field(name = '?ping', value = 'Visualiza a latência do Bot.\nEx: ?ping', inline= False)

    return embed

#**************************************************************************************************************#
#Embed de erro - Usado no remover.py / add.py / retirar.py

def erro(nome):

    embed = discord.Embed(
        title = f'O {nome} não está no jogo!',
        color = 0x22a7f0
    )
    embed.set_footer(text = '?help para ajuda')
    embed.add_field(name = 'Dica:', value = 'Use o ?pontos pra verificar o nome dos participantes.', inline = False)

    return embed

#**************************************************************************************************************#