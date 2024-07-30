'''
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''
import os
from time import sleep

def limpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def line(prompt, width=60):
    prompt = f'\n{prompt:^{width}}'
    print(prompt)

matriz = [[],[],[]]

for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))
    print('-'*50)

somaPar = 0
somaTerCol = 0
maiorSegLinha = 0

for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
        if c == 2:
            somaTerCol += matriz[l][c]
        if l == 1:
            if c == 0:
                maiorSegLinha = matriz[l][c]
            elif matriz[l][c] > maiorSegLinha:
                maiorSegLinha = matriz[l][c]
sleep(1)
limpaTela()
line('Matriz 3x3\n', 60)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^7}]', end='')
    print()
line('Analise da soma e maior valor', 60)
print(f'\nA) Soma de todos os valores pares: {somaPar}.')
print(f'B) Soma dos valores da terceira coluna: {somaTerCol}.')
print(f'C) Maior valor da segunda linha: {maiorSegLinha}.\n')