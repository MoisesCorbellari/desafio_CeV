'''
Crie um programa que declare uma matriz de dimensão 3x3 
e preencha com valores lidos pelo teclado. 
No final, mostre a matriz na tela, com a formatação correta.
'''
def line(prompt, width=60):
    prompt = f'\n{prompt:^{width}}'
    print(prompt)
        
matriz = [[],[],[]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))
    print('-='*30)

line('Matriz 3x3\n', 60)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()