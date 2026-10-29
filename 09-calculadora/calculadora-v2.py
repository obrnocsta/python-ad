import os
from colors import *

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_mensagem(texto, cor_borda=FRENTE_VERDE_CLARO):
    """Exibe mensagens de retorno do sistema em caixas estilizadas."""
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
    print(f"{borda}║              CALCULADORA             ║{RESET}")
    print(f"{borda}╠══════════════════════════════════════╣{RESET}")
    print(f"{borda}║ {num}1.{RESET} {txt}Soma (+)                          {borda}║{RESET}")
    print(f"{borda}║ {num}2.{RESET} {txt}Subtração (-)                     {borda}║{RESET}")
    print(f"{borda}║ {num}3.{RESET} {txt}Multiplicação (*)                 {borda}║{RESET}")
    print(f"{borda}║ {num}4.{RESET} {txt}Divisão (/)                       {borda}║{RESET}")
    print(f"{borda}║ {num}5.{RESET} {txt}Sair                              {borda}║{RESET}")
    print(f"{borda}╚══════════════════════════════════════╝{RESET}")

def coletar_numeros():
    numeros = []
    print(FRENTE_CINZA + "\nDigite os números em sequência. Digite 0 para encerrar." + RESET)
    
    while True:
        try:
            entrada = float(input(FRENTE_BRANCO_CLARO + f"Número {len(numeros) + 1}: " + RESET))
            if entrada == 0:
                break
            numeros.append(entrada)
        except ValueError:
            print(FRENTE_VERMELHO_CLARO + "Entrada inválida. Digite apenas números." + RESET)
            
    return numeros

def calcular(operacao):
    opcoes_nome = {"1": "SOMA", "2": "SUBTRAÇÃO", "3": "MULTIPLICAÇÃO", "4": "DIVISÃO"}
    print(FRENTE_AMARELO_CLARO + ESTILO_NEGRITO + f"\n--- {opcoes_nome[operacao]} ---" + RESET)
    
    numeros = coletar_numeros()
    
    if not numeros:
        exibir_mensagem("Nenhum número foi inserido.", FRENTE_VERMELHO_CLARO)
        return

    if operacao == "1":
        resultado = sum(numeros)
    elif operacao == "2":
        resultado = numeros[0]
        for n in numeros[1:]:
            resultado -= n
    elif operacao == "3":
        resultado = 1
        for n in numeros:
            resultado *= n
    elif operacao == "4":
        resultado = numeros[0]
        for n in numeros[1:]:
            if n == 0:
                exibir_mensagem("Não é possível dividir por zero.", FRENTE_VERMELHO_CLARO)
                return
            resultado /= n

    if resultado.is_integer():
        res_formatado = int(resultado)
    else:
        res_formatado = f"{resultado:.2f}".rstrip('0').rstrip('.')

    exibir_mensagem(f"Resultado final: {res_formatado}", FRENTE_VERDE_CLARO)

opcao = ""
while opcao != "5":
    menu()
    opcao = input(FRENTE_MAGENTA_CLARO + ESTILO_NEGRITO + "\nEscolha uma opção: " + RESET).strip()

    if opcao in ["1", "2", "3", "4"]:
        calcular(opcao)
    elif opcao == "5":
        exibir_mensagem("Encerrando a calculadora...", FRENTE_AZUL_CLARO)
        break
    else:
        exibir_mensagem("Opção inválida. Tente novamente.", FRENTE_VERMELHO_CLARO)

    input(FRENTE_CINZA + "\nPressione ENTER para continuar..." + RESET)
