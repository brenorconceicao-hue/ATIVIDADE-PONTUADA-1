import os 
os.system ('cls')

cor = input("Digite a cor do CD (Verde, Azul, Amarelo, Vermelho): ").strip().capitalize()

match cor:
    case "Verde":
        preco = 10.00
    case "Azul":
        preco = 20.00
    case "Amarelo":
        preco = 30.00
    case "Vermelho":
        preco = 40.00
    case _:
        preco = None

if preco is not None:
    print(f"O preço do CD {cor} é: R$ {preco:.2f}")
else:
    print("Cor inválida.")