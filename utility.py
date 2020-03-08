import json
from datetime import datetime

def capitalizacao(msg):
    return msg.lower().capitalize()

def hora():
    return datetime.now().strftime('%d/%m/%Y - %H:%M:%S')

def organizar():

    with open('pontos.json', 'r') as f:
        pontos = json.load(f)

    for i in range(len(pontos['Nomes'])):
        for j in range(len(pontos['Nomes'])):
            if pontos['Pontos'][i] > pontos['Pontos'][j]:
                
                a = pontos['Pontos'][i]
                b = pontos['Nomes'][i]

                pontos['Pontos'][i] = pontos['Pontos'][j]
                pontos['Nomes'][i] = pontos['Nomes'][j]

                pontos['Pontos'][j] = a
                pontos['Nomes'][j] = b

    with open('pontos.json', 'w') as f:
        json.dump(pontos, f, indent= 4)