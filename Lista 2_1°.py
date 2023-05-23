n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))


med = (n1 + n2 + n3 + n4) / 4

if med < 4:
    situacao = "Em processo de Aprendizagem (Reprovado)"
elif med < 8:
    situacao = "Recuperação"
else:
    situacao = "Aprovado"

print("Situação do aluno:", situacao)
