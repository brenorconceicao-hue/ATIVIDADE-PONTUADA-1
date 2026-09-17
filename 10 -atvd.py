import os 
os.system('cls')

nome = input("Digite o nome: ")
sexo = input("Digite o sexo (M/F): ")
estado_civil = input("Digite o estado civil: ")

tempo_casada = None

match (sexo, estado_civil):
    case ("F", "CASADA"):
        tempo_casada = int(input("Digite o tempo de casada (em anos): "))

print("\n--- DADOS DO USUÁRIO ---")
print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")

if tempo_casada is not None:
    print(f"Tempo de casada: {tempo_casada} anos")