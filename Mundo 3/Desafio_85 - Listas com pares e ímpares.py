'''
Crie um programa onde o usuário possa digitar sete valores numéricos e 
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.
'''

pares = []
impares = []

def line(txt, width=60):
    prompt = f'\n{txt:^{width}}'
    print(prompt)
    print('-'*width)

for p in range(0,7):
    num = int(input(f'Digite o {p+1}º valor: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
pares.sort()
impares.sort()
line('Lista com pares e impares', 60)
print(f'\n-> Valores pares digitados: {pares}.')
print(f'-> Valores ímpares digitados: {impares}.\n')