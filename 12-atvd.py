import os 
os.system('cls')

kg_morango = float(input("Digite a quantidade de morangos (Kg): "))
kg_maca = float(input("Digite a quantidade de maçãs (Kg): "))

if kg_morango <= 5:
    preco_morango = 2.50
else:
    preco_morango = 2.20


if kg_maca <= 5:
    preco_maca = 1.80
else:
    preco_maca = 1.50

valor_total = (kg_morango * preco_morango) + (kg_maca * preco_maca)
peso_total = kg_morango + kg_maca

if peso_total >= 10 or valor_total > 15.00:
    valor_total *= 0.90

print(f"\nValor a ser pago pelo cliente: R$ {valor_total:.2f}")