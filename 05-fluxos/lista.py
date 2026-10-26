aprovados = ["bruno", "jessica", "renata", "cesar"]

candidato = input("Nome: ").strip().lower()

aprovados_minusculo = [nome.lower() for nome in aprovados]

if candidato in aprovados_minusculo:
	print(f"'{candidato.title()}', aprovado(a)!")
else:
	print(f"'{candidato.title()}', reprovado(a)...")

#aprovados = ["bruno", "jessica", "renata", "cesar"]

#candidato = input("Nome: ").strip()

#if candidato.lower() in [n.lower() for n in aprovados]:
#	print(f"'{candidato}' aprovado(a)!")
#else:
#	print(f"'{candidato}', não reprovado(a)...")
