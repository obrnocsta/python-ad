from colors import *

tarefas = []

def menu():
	print(FRENTE_AMARELO + "########## MENU ##########" + RESET)
	print("1 - Adicionar")
	print("2 - Listar")
	print("3 - Remover")
	print("4 - Sair")

def adicionar():
	tarefa = input("Tarefa: ")
	tarefas.append(tarefa)
	print("Tarefa adicionarda")


def listar():
	if len(tarefas) == 0:
		print("Tarefas vazia")
	else:
		for numero, tarefa in enumerate(tarefas, start=1):
			print(numero, tarefa, sep=("-"))

def remover():
	listar()

	if len(tarefas) > 0:
		numero = int(input("Id: "))
		if 1 <= numero <= len(tarefas):
			tarefas.pop(numero - 1)
			print("Tarefa removida")
		else:
			print("Tarefa não encontrada")

opcao = ""
while opcao != "4":
	menu()
	opcao = input("Opção: ")

	if opcao == "1":
		adicionar()
	elif opcao == "2":
		listar()
	elif opcao == "3":
		remover()
	elif opcao == "4":
		print("Saindo...")
	else: 
		print("Opção inválida")
