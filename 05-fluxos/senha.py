senha_correta = "turmaad05"
tentativas = 0
limite_tentativas = 3

while tentativas < limite_tentativas:
	senha = input("Senha: ")
	
	if senha == senha_correta:
		print("Acesso liberado!")
		break
	else:
		tentativas += 1
		tentativas_restantes = limite_tentativas - tentativas
		print("Acesso negado...\n")

		if tentativas_restantes > 0:
			print(f"Tentativas restantes: {tentativas_restantes}")

if senha != senha_correta:
	print("Acesso bloqueado.")

#senha = ""

#tentativas = 3
#while senha != "turmaad05":
#	tentativas -= 1
#	print(tentativas)
#	print("Acesso negado...")
#	senha = input("Senha: ")

#print("Acesso liberado!")
