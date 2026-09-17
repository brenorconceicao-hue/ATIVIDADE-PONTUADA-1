import os 
os.system('cls')

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

soma = a + b

if soma < c:
    print("A soma de A + B é menor que C")
elif soma > c:
    print("A soma de A + B é maior que C")
else:
    print("A soma de A + B é igual a C")