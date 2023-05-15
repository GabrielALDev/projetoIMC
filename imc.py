print('Este é um programa que calcula seu IMC - Indice de Massa Corporal')
print('Vamos calcular seu IMC?')

peso = float(input('Qual o seu peso? '))
altura = float(input('Qual sua altura? '))

imc = peso / (altura * altura)

if imc <= 18.5:
    print(f'Seu IMC é: {imc:.2f} Você está com magreza')
elif (imc >= 18.5) and (imc <= 24.9):
    print(f'Seu IMC é: {imc:.2f} Você está com o peso normal')
elif (imc >= 25) and (imc <= 29.9):
    print(f'Seu IMC é: {imc:.2f} Você está com sobrepeso')
elif (imc >= 30) and (imc <= 34.9):
    print(f'Seu IMC é: {imc:.2f} Você está com obsidade grau I')
elif (imc >= 35) and (imc <= 39.9):
    print(f'Seu IMC é: {imc:.2f} Você está com obsidade grau II')
else:
    print('Você está com obsidade grau III')