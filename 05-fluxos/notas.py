nome = input("Nome do (a) aluno(a): ")

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2

situacao = ""

if media >= 7:
	situacao = "aprovado(a)"
elif media >= 5:
	situacao = "exame"
else:
	situacao = "reprovado(a)"

print(f"Aluno(a) {nome}, {situacao} com média {media}.")
