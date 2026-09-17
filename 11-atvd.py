import os 
os.system('cls')

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

match (A == B):
    case True:
        C = A + B
    case False:
        C = A * B

print(f"O resultado na variável C é: {C}")