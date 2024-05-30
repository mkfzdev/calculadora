print('Operações: ')
print('1. Adição')
print('2. Subtração')
print('3. Multiplicação')
print('4. Divisão')

operacao = input('Selecione a operação 1/2/3/4: ')

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

if operacao == '1':
    resultado = numero1 + numero2

elif operacao == '2':
    resultado = numero1 - numero2

elif operacao == '3':
    resultado = numero1 * numero2

elif operacao == '4':
    resultado = numero1 / numero2

print('O resultado da operação é: ' + str(resultado))
