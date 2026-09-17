import os 
os.system('cls')

PRECO_ALCOOL = 3.79
PRECO_GASOLINA = 6.59

litros = float(input("Digite o número de litros vendidos: "))
tipo = input("Digite o tipo de combustível (A-Álcool, G-Gasolina): ")

match (tipo, litros <= 25):
    case ("A", True):
        desconto = 0.10
    case ("A", False):
        desconto = 0.20
    case ("G", True):
        desconto = 0.15
    case ("G", False):
        desconto = 0.30
    case _:
        desconto = 0

match tipo:
    case "A":
        preco_base = PRECO_ALCOOL
    case "G":
        preco_base = PRECO_GASOLINA
    case _:
        preco_base = 0

valor_sem_desconto = litros * preco_base
valor_final = valor_sem_desconto * (1 - desconto)

match preco_base:
    case 0:
        print("Tipo de combustível inválido!")
    case _:
        print(f"\nTotal a pagar: R$ {valor_final:.2f}")