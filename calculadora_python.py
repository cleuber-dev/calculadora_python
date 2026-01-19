# -------------Calculadora básica em Python----------------


on_off = 'on'

while on_off == 'on':
    number1 = float(input('Digite o primeiro número: '))
    operator = input('Digite o operador (+, -, *, /): ')
    number2 = float(input('Digite o segundo número: '))

    if operator == '+':
        result = number1 + number2


    elif operator == '-':
        result = number1 - number2


    elif operator == '*':
        result = number1 * number2


    elif operator == '/':
        if number2 == 0:
            print('Não existe divisão por zero!')
        else:
            result = number1 / number2


    else:
        print('Você digitou algum operador inválido.')

    if result.is_integer():
        print(int(result))
    else:
        print(result)

    on_off = input('Digite "on" para realizar outro cálculo ou qualquer outra coisa para sair: ')
print()
print('Calculadora Desligada')