'''
Calculadora de IMC: Crie um programa que recebe o peso e a altura de uma pessoa e calcula seu Índice de Massa Corporal (IMC), exibindo uma mensagem de acordo com a faixa de peso (abaixo do peso, peso normal, sobrepeso, etc.).
'''

def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    return imc

print("Tabela de IMC e Categorias de Peso:")
print("| IMC             | Categoria           |")
print("|-----------------|---------------------|")
print("| Abaixo de 18,5  | Abaixo do peso      |")
print("| 18,5 - 24,9     | Peso normal         |")
print("| 25,0 - 29,9     | Sobrepeso           |")
print("| 30,0 - 34,9     | Obesidade grau I    |")
print("| 35,0 - 39,9     | Obesidade grau II   |")
print("| Acima de 40,0   | Obesidade grau III  |")

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = calcular_imc(peso, altura)
imc = round(imc, 2)

if imc < 18.5:
    print(f"Seu imc é {imc} então você está abaixo do peso")

elif imc <= 24.9:
    print(f"Seu imc é {imc} então você está no peso normal")

elif  imc <= 29.9:
    print(f"Seu imc é {imc} então você está com sobrepeso")

elif  imc <= 34.9:
    print(f"Seu imc é {imc} então você está Obesidade grau I")

elif  imc <= 39.9:
    print(f"Seu imc é {imc} então você está com Obesidade grau II")
else:
    print(f"Seu imc é {imc} então você está com Obesidade grau III")