import os 
os.system ('cls')

renda_mensal = float(input("Digite a renda mensal: R$ "))
valor_emprestimo = float(input("Digite o valor do empréstimo solicitado: R$ "))
n_prestacoes = int(input("Digite o número de prestações: "))

valor_prestacao = valor_emprestimo / n_prestacoes

limite_emprestimo = renda_mensal * 10
limite_prestacao = renda_mensal * 0.30


limite_emprestimo_ok = valor_emprestimo <= limite_emprestimo
limite_prestacao_ok = valor_prestacao <= limite_prestacao

match (limite_emprestimo_ok, limite_prestacao_ok):
    case (True, True):
        print  ("Empréstimo concedido.")
    case _:
        print = ("Empréstimo negado.")

print(f"\n--- resultado ---")
print(f"Valor da prestação: R$ {valor_prestacao:.2f}")
