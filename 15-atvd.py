import os 
os.system('cls')

nome = input("Digite a descrição do produto: ")
quantidade = int(input("Digite a quantidade adquirida: "))
preco_unitario = float(input("Digite o preço unitário: R$ "))

total = quantidade * preco_unitario

match quantidade:
    case q if q <= 5:
        percentual_desconto = 0.02
    case q if q <= 10:
        percentual_desconto = 0.03
    case _:
        percentual_desconto = 0.05

desconto = total * percentual_desconto
total_a_pagar = total - desconto

print(f"\n--- compras ---")
print(f"Produto: {nome}")
print(f"Total bruto: R$ {total:.2f}")
print(f"Desconto ({int(percentual_desconto * 100)}%): R$ {desconto:.2f}")
print(f"Total a pagar: R$ {total_a_pagar:.2f}")