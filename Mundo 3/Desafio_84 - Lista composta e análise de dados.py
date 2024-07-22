'''Faça um programa que leia nome e peso de várias pessoas,                                      
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

import os
from time import sleep

pessoas = []
pessoas1 = []
counter = 0

def line(txt, width=60):
    prompt = f'\n{txt:^{width}}'
    print(prompt)
    print('-'*width)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

line('Análise de dados:', 60)

while True:
    pessoas.append(str(input('Nome: '))) # Adicionando nome à lista
    pessoas.append(float(input('Peso (kg): '))) # Adicionando peso à lista
    
    pessoas1.append(pessoas[:]) # Adicionando a lista de pessoas ao final da lista
    pessoas.clear()
    counter += 1

    resp = input('Continuar? (S/N): ')
    print('_'*60)
    if resp.upper() == 'N':
        print('\nPrograma encerrado.')
        sleep(1)
        break

print()

clear_screen()

line('Listagem dos dados:', 60)
print(f'\nA) Quantas pessoas foram cadastradas: {counter}') 

peso = list()

for i in pessoas1:
    peso.append(i[1])

peso = sorted(peso, reverse=True) # Ordenando os pesos em ordem decrescente

pesados = peso[0] # Pessoas mais pesada
leves = peso[-1] # Pessoas mais leve

max_peso = list()
min_peso = list()

for pessoa in pessoas1:
    if pessoa[1] == pesados:
        max_peso.append(pessoa) 
    elif pessoa[1] == leves:
        min_peso.append(pessoa)

print('\nB) Pessoas mais pesadas:')
for pessoa in max_peso:
    print(f'Nome: {pessoa[0]}, Peso: {pessoa[1]}kg')

print('\nC) Pessoas mais leves:')
for pessoa in min_peso:
    print(f'Nome: {pessoa[0]}, Peso: {pessoa[1]}kg\n')