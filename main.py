import discord
import asyncio
from datetime import datetime

bot = discord.Client()
lista_nomes = []
lista_pontos = []
lista_nomevar = []
lista_votovar = []
num_p, num_n = 0, 0
confirm_var = False

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

    if message.content.lower().startswith('?ping'):
        ping_embed = discord.Embed(
            title = '⌛️ %i ms' %int((bot.latency * 1000)),
            color = 0x22a7f0
        )
        ping_embed.set_footer(text = '?help para ajuda')
        await message.channel.send(embed = ping_embed)
        print(hora() + ' - ' + message.author.name + ' pingou.')

    if message.content.lower().startswith('?novo'):
        nome = capitalizacao(message.content[6:])
        if nome in lista_nomes:
            novo_embedt = discord.Embed(
                title = 'O nome ' + nome + ' já foi adicionado ao jogo.',
                color = 0x22a7f0
            )
            novo_embedt.set_footer(text = '?help para ajuda')
            await message.channel.send(embed = novo_embedt)
            print(hora() + ' - ' + message.author.name + ' tentou adicionar o ' + nome + ' novamente ao jogo.')
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
            print(hora() + ' - ' + message.author.name + ' adicionou o ' + nome + ' ao jogo.')
                 
    if message.content.lower().startswith('?pontos'):
        if len(lista_nomes) == 0:
            pnt_embedf = discord.Embed(
                title = 'Não há ninguém no jogo!',
                color = 0x22a7f0
            )
            pnt_embedf.set_footer(text = '?help para ajuda')
            await message.channel.send(embed = pnt_embedf)
            print(hora() + ' - ' + message.author.name + ' solicitou a listagem dos pontos dos participantes do jogo, mas não tinha ninguém participando.')
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
            print(hora() + ' - ' + message.author.name + ' solicitou a listagem dos pontos dos participantes do jogo.')

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
            print(hora() + ' - ' + message.author.name + ' retirou o ' + nome + ' do jogo.')

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
            print(hora() + ' - ' + message.author.name + ' tentou adicionar 0 pontos do ' + nome + '.')
        else:
            verif = False
            try:
                pos = lista_nomes.index(nome)
                verif = True
            except ValueError:
                await erro_nome(message)
                if numero == 1:
                    print(hora() + ' - ' + message.author.name + ' tentou adicionar 1 ponto ao ' + nome + ', mas não tinha ninguém com esse nome.')
                else:
                    print(hora() + ' - ' + message.author.name + ' tentou adicionar ' + numero + ' pontos ao ' + nome + ', mas não tinha ninguém com esse nome.')
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
                    print(hora() + ' - ' + message.author.name + ' adicionou 1 ponto ao ' + nome + ', ele tem ' + str(lista_pontos[pos]) + ' agora.')
                else:
                    await message.channel.send(embed = addt_embedp)
                    print(hora() + ' - ' + message.author.name + ' adicionou ' + numero + ' pontos ao ' + nome + ', ele tem ' + str(lista_pontos[pos]) + ' agora.')

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
            print(hora() + ' - ' + message.author.name + ' tentou retirar 0 pontos do ' + nome + '.')
        else:
            verif = False
            try:
                pos = lista_nomes.index(nome)
                verif = True
            except ValueError:
                await erro_nome(message)
                if numero == '1':
                    print(hora() + ' - ' + message.author.name + ' tentou retirar 1 ponto ao ' + nome + ', mas não tinha ninguém com esse nome.')
                else:
                    print(hora() + ' - ' + message.author.name + ' tentou retirar ' + numero + ' pontos ao ' + nome + ', mas não tinha ninguém com esse nome.')
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
                        print(hora() + ' - ' + message.author.name + ' tentou retirar 1 ponto ao ' + nome + ', mas ele já tinha 0 pontos.')
                    else:
                        print(hora() + ' - ' + message.author.name + ' tentou retirar ' + numero + ' pontos ao ' + nome + ', mas ele já tinha 0 pontos.')
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
                        print(hora() + ' - ' + message.author.name + ' retirou 1 ponto ao ' + nome + ', ele tem ' + str(lista_pontos[pos]) + ' agora.')
                    else:
                        await message.channel.send(embed = retirar_embedp)
                        print(hora() + ' - ' + message.author.name + ' retirou ' + numero + ' pontos ao ' + nome + ', ele tem ' + str(lista_pontos[pos]) + ' agora.')

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
        help_embed.add_field(name = '?var', value = 'Inicia uma votação. (Necessário 5 votos para anular ou confirmar um var.)\nEx: ?var "motivo"', inline = False)
        help_embed.add_field(name = '?cancelarvar', value = 'Cancela o var que você criou. (Somente a pessoa que iniciou o var pode cancela-lo).\nEx: ?cancelarvar', inline = False)
        help_embed.add_field(name = '?ping', value = 'Visualiza a latência do Bot.\nEx: ?ping', inline= False)
        await message.channel.send(embed = help_embed)
        print(hora() + ' - ' + message.author.name + ' usou o ?help.')

    if message.content.lower().startswith('?reset'):
        if len(lista_nomes) != 0:
            if message.author.id == 232142342591741952:
                reset_embedt = discord.Embed(
                    title = 'Os nomes e pontos foram limpos!',
                    color = 0x22a7f0
                )
                await message.channel.send(embed = reset_embedt)
                print(hora() + ' - ' + message.author.name + ' resetou o jogo.')
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
                print(hora() + ' - ' + message.author.name + ' tentou resetar o jogo.')
        else:
            reset_embedff = discord.Embed(
                title = 'Não há ninguém no jogo!',
                color = 0x22a7f0
            )
            reset_embedff.set_footer(text = '?help para ajuda')
            await message.channel.send(embed = reset_embedff)
            print(hora() + ' - ' + message.author.name + ' tentou resetar o jogo, mas não tinha ninguém participando.')

    if message.content.lower().startswith('?var'):
        motivo = message.content[5:]
        motivo_embed = discord.Embed(
            title = 'Nova votação criada:',
            color = 0x22a7f0
        )
        motivo_embed.set_footer(text = '?help para ajuda')
        motivo_embed.add_field(name = message.author.name + ' criou a votação', value = motivo, inline=False)
        msg_bot = await message.channel.send(embed = motivo_embed)
        print(hora() + ' - ' + message.author.name + ' criou um novo var.')
        global autor_var
        autor_var = message.author.name
        global confirm_var
        confirm_var = True
        global var_mensagem
        var_mensagem = message
        global msg_id
        msg_id = msg_bot.id
        await msg_bot.add_reaction('✅')
        await msg_bot.add_reaction('❌')

    if message.content.lower().startswith('?cancelarvar'):
        global num_p
        global num_n
        if confirm_var and message.author.name == autor_var:
            cancelvar_embed = discord.Embed(
                title = 'O var foi cancelado!',
                color = 0x22a7f0
            )
            cancelvar_embed.set_footer(text = '?help para ajuda')
            await message.channel.send(embed = cancelvar_embed)
            print(hora() + ' - ' + message.author.name + ' cancelou seu var.')
            lista_nomevar.clear()
            lista_votovar.clear()
            num_n, num_p = 0, 0
            msg_id = None
            confirm_var = False
        else:
            if not confirm_var:
                semvar_embed = discord.Embed(
                    title = 'Não existe uma votação em andamento!',
                    color =  0x22a7f0
                )
                semvar_embed.set_footer(text = '?help para ajuda')
                await message.channel.send(embed = semvar_embed)
                print(hora() + ' - ' + message.author.name + ' tentou cancelar um var que não existe.')
            else:
                autorcancel_embed = discord.Embed(
                    title = 'Não foi você que iniciou essa votação!',
                    color = 0x22a7f0
                )
                autorcancel_embed.set_footer(text = '?help para ajuda')
                await message.channel.send(embed = autorcancel_embed)
                print(hora() + ' - ' + message.author.name + ' tentou cancelar um var que não iniciou.')
               
@bot.event
async def on_reaction_add(reaction, user):
    global num_n
    global num_p
    global var_mensagem
    global confirm_var
    global msg_id
    if msg_id == reaction.message.id and not user.name in lista_nomevar and user.name != 'BotPontosTest':
        lista_nomevar.append(user.name)
        lista_votovar.append(reaction.emoji)
        if num_p < 5 and num_n < 5:
            if reaction.emoji == '✅':
                votopadd_embed = discord.Embed(
                    title = user.name + ' votou ' + reaction.emoji,
                    color = 0x22a7f0
                )
                votopadd_embed.set_footer(text = '?help para ajuda')
                await var_mensagem.channel.send(embed = votopadd_embed)
                print(hora() + ' - ' + user.name + ' votou favoravelmente ao var.')
                num_p = reaction.count - 1
            elif reaction.emoji == '❌':
                votonadd_embed = discord.Embed(
                    title = user.name + ' votou ' + reaction.emoji,
                    color = 0x22a7f0
                )
                votonadd_embed.set_footer(text = '?help para ajuda')
                await var_mensagem.channel.send(embed = votonadd_embed)
                print(hora() + ' - ' + user.name + ' votou negativamente ao var.')
                num_n = reaction.count - 1
            print(num_n)
            print(num_p)
        else:
            if num_p == 5:
                confirm = 'Confirmado!'
            else:
                confirm = 'Anulado!'
            finalvar_embed = discord.Embed(
                title = 'Resultado do var:',
                color = 0x22a7f0                   
            )
            finalvar_embed.set_footer(text = '?help para ajuda')
            for i in range (len(lista_nomevar)):
                finalvar_embed.add_field(name = lista_nomevar[i], value = lista_votovar[i], inline = False)
            finalvar_embed.add_field(name = '\nO resultado final é: ', value = confirm, inline= False)
            await var_mensagem.channel.send(embed = finalvar_embed)
            print(hora() + ' - Finalizado as votações do var: ' + confirm)
            confirm_var = False
            lista_nomevar.clear()
            lista_votovar.clear()
            num_n, num_p = 0, 0
    else:
        if user.name in lista_nomevar:
            pos = lista_nomevar.index(user.name)
            votoduplicado_embed = discord.Embed(
                title = 'Você já votou nesse var: ' + lista_nomevar[pos] + ' --> ' + lista_votovar[pos],
                color = 0x22a7f0 
            )
            votoduplicado_embed.set_footer(text = '?help para ajuda')
            await var_mensagem.channel.send(embed = votoduplicado_embed)
            print(hora() + ' - ' + var_mensagem.author.name + ' tentou votar em duas opções.')

@bot.event
async def on_reaction_remove(reaction, user):
    global num_p
    global num_n
    global var_mensagem
    try:
        pos = lista_nomevar.index(user.name)
        verif = True
    except ValueError:
        verif = False
    if verif:
        emoji_react = lista_votovar[pos]
        if reaction.emoji == emoji_react:
            votoremovido_embed = discord.Embed(
                title = 'O voto ' + lista_votovar[pos] + ' do ' + lista_nomevar[pos] + ' foi removido',
                color = 0x22a7f0
            )
            votoremovido_embed.set_footer(text = '?help para ajuda')
            await var_mensagem.channel.send(embed = votoremovido_embed)
            print(hora() + ' - ' + user.name + ' retirou o voto dele.')
            del(lista_nomevar[pos])
            del(lista_votovar[pos])

bot.run('Njc5MTUzNzU0MTc1NzAxMDMy.XllkjA.03YWg6le-yv4GhaFEzuiiKjwW-U')