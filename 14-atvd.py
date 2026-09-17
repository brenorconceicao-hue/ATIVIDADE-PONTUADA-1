import os 
os.system('cls')

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print(f"\nMédia: {media:.1f}")

match media:
    case m if m >= 6.0:
        print("Parabéns , Você foi aprovado")
    case m if 4.1 <= m <= 5.9:
        print("Aluno em recuperação.")
    case _:
        print("Aluno reprovado.")