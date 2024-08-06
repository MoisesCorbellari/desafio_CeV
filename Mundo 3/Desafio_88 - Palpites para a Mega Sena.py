'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta.
'''

from random import randint
from time import sleep
import os

def line(txt, width=60):
    print('-' * 60)
    print(txt.center(width))
    print('-' * 60)

def limpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')

jogos = list()
tot = 1

limpaTela()
line('Palpites criados para Mega Sena', 60)
qtdjogos= int(input('Quantos jogos serão criados? '))
print()

while tot <= qtdjogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogos:
            jogos.append(num)
            cont += 1
        if cont >= 6:
            break
    print(f'{tot}º palpite: {jogos}')
    tot += 1
    jogos.clear()
    sleep(1)
print()