num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operador = input("Digite o operador (+, -, *, /): ").strip()

if operador not in ['+', '-', '*', '/']:
    print("Operador inválido")

elif operador == '/' and num2 == 0:
    print("Não é possível dividir por zero")
else:
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        resultado = num1 / num2
    
    if resultado.is_integer():
        print(int(resultado))
    else:
        print(resultado)
