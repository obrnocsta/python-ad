import os
from colors import *

tarefas = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_mensagem(texto, cor_borda=FRENTE_VERDE_CLARO):
    """Exibe mensagens de retorno do sistema envolvidas por uma moldura."""
    largura = len(texto) + 4
    borda = cor_borda + ESTILO_NEGRITO
    print(f"\n{borda}┌" + "─" * largura + "┐" + RESET)
    print(f"{borda}│  {RESET}{cor_borda}{texto}{RESET}{borda}  │{RESET}")
    print(f"{borda}└" + "─" * largura + "┘" + RESET)

def menu():
    limpar_tela()
    borda = FRENTE_AMARELO_CLARO + ESTILO_NEGRITO
    txt = FRENTE_BRANCO_CLARO
    num = FRENTE_CIANO_CLARO + ESTILO_NEGRITO
    
    print(f"{borda}╔══════════════════════════════════════╗{RESET}")
    print(f"{borda}║           PAINEL DE TAREFAS          ║{RESET}")
    print(f"{borda}╠══════════════════════════════════════╣{RESET}")
    print(f"{borda}║ {num}1.{RESET} {txt}Adicionar tarefa                  {borda}║{RESET}")
    print(f"{borda}║ {num}2.{RESET} {txt}Listar tarefas                    {borda}║{RESET}")
    print(f"{borda}║ {num}3.{RESET} {txt}Remover tarefa                    {borda}║{RESET}")
    print(f"{borda}║ {num}4.{RESET} {txt}Sair                              {borda}║{RESET}")
    print(f"{borda}╚══════════════════════════════════════╝{RESET}")

def adicionar():
    print(FRENTE_AMARELO_CLARO + ESTILO_NEGRITO + "\n--- NOVAL TAREFA ---" + RESET)
    tarefa = input(FRENTE_BRANCO_CLARO + "Digite a descrição: " + RESET).strip()
    
    if tarefa:
        tarefas.append(tarefa)
        exibir_mensagem(f"Tarefa '{tarefa}' adicionada!", FRENTE_VERDE_CLARO)
    else:
        exibir_mensagem("A descrição não pode ser vazia.", FRENTE_VERMELHO_CLARO)

def listar():
    if not tarefas:
        exibir_mensagem("Nenhuma tarefa cadastrada.", FRENTE_VERMELHO_CLARO)
    else:
        borda = FRENTE_CIANO_CLARO + ESTILO_NEGRITO
        print(f"\n{borda}┌─ LISTA DE TAREFAS ───────────────────┐{RESET}")
        for numero, tarefa in enumerate(tarefas, start=1):
            num_formatado = f"{FRENTE_AMARELO_CLARO}{ESTILO_NEGRITO}{numero:2d}.{RESET}"
            print(f"{borda}│{RESET} {num_formatado} {FRENTE_BRANCO_CLARO}{tarefa}{RESET}")
        print(f"{borda}└──────────────────────────────────────┘{RESET}")

def remover():
    listar()
    if tarefas:
        entrada = input(FRENTE_BRANCO_CLARO + ESTILO_NEGRITO + "\nNúmero da tarefa a remover: " + RESET)
        
        if entrada.isdigit():
            numero = int(entrada)
            if 1 <= numero <= len(tarefas):
                removida = tarefas.pop(numero - 1)
                exibir_mensagem(f"Tarefa '{removida}' removida!", FRENTE_VERDE_CLARO)
            else:
                exibir_mensagem("Número fora da lista.", FRENTE_VERMELHO_CLARO)
        else:
            exibir_mensagem("Entrada inválida. Digite um número.", FRENTE_VERMELHO_CLARO)

# Loop Principal
opcao = ""
while opcao != "4":
    menu()
    opcao = input(FRENTE_MAGENTA_CLARO + ESTILO_NEGRITO + "\nEscolha uma opção: " + RESET).strip()

    if opcao == "1":
        adicionar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        remover()
    elif opcao == "4":
        exibir_mensagem("Encerrando o sistema...", FRENTE_AZUL_CLARO)
        break
    else:
        exibir_mensagem("Opção inválida. Tente novamente.", FRENTE_VERMELHO_CLARO)

    input(FRENTE_CINZA + "\nPressione ENTER para continuar..." + RESET)
