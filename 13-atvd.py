import os 
os.system('cls')

operacao = input("Digite a operação (+, -, *, /): ")
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

match operacao:
    case "+":
        resultado = a + b
    case "-":
        resultado = a - b
    case "*":
        resultado = a * b
    case "/":
        resultado = a / b
    case _:
        resultado = "Operação inválida"

print(f"\nResultado: {resultado}")