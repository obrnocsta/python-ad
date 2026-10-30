import os
import math
from colors import *

def somarmultiplosnumeros(numeros):
    return math.fsum(numeros)

def multiplicarmultiplosnumeros(numeros):
    return math.prod(numeros)

def ehpar(numero):
    return numero % 2 == 0

def ehinteiro(numero):
    if isinstance(numero, float):
        return numero.is_integer()
    return isinstance(numero, int)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_mensagem(texto, cor_borda=FRENTE_VERDE_CLARO):
    largura = len(texto) + 4
    borda = cor_borda + ESTILO_NEGRITO
    print(f"\n{borda}┌" + "─" * largura + "┐" + RESET)
    print(f"{borda}│  {RESET}{cor_borda}{texto}{RESET}{borda}  │{RESET}")
    print(f"{borda}└" + "─" * largura + "┘" + RESET)

def formatar_numero(val):
    if isinstance(val, float) and val.is_integer():
        return int(val)
    return val

def coletar_lista_numeros():
    numeros = []
    print(FRENTE_CINZA + "\nDigite os números sequencialmente. Digite 'fim' para encerrar a lista." + RESET)
    
    while True:
        entrada = input(FRENTE_BRANCO_CLARO + f"Número {len(numeros) + 1}: " + RESET).strip()
        if entrada.lower() == 'fim':
            break
        try:
            val = float(entrada)
            numeros.append(formatar_numero(val))
        except ValueError:
            print(FRENTE_VERMELHO_CLARO + "Entrada inválida! Digite um número ou 'fim'." + RESET)
            
    return numeros

def coletar_unico_numero(mensagem="Digite um número: "):
    while True:
        try:
            val = float(input(FRENTE_BRANCO_CLARO + mensagem + RESET))
            return formatar_numero(val)
        except ValueError:
            print(FRENTE_VERMELHO_CLARO + "Entrada inválida! Digite um número válido." + RESET)

def tela_operacoes_lote():
    while True:
        limpar_tela()
        borda = FRENTE_CIANO_CLARO + ESTILO_NEGRITO
        txt = FRENTE_BRANCO_CLARO
        num = FRENTE_AMARELO_CLARO + ESTILO_NEGRITO

        print(f"{borda}╔══════════════════════════════════════╗{RESET}")
        print(f"{borda}║         OPERAÇÕES EM LOTE            ║{RESET}")
        print(f"{borda}╠══════════════════════════════════════╣{RESET}")
        print(f"{borda}║ {num}1.{RESET} {txt}Somar lista de números            {borda}║{RESET}")
        print(f"{borda}║ {num}2.{RESET} {txt}Multiplicar lista de números      {borda}║{RESET}")
        print(f"{borda}║ {num}3.{RESET} {txt}Voltar ao menu principal          {borda}║{RESET}")
        print(f"{borda}╚══════════════════════════════════════╝{RESET}")

        sub_opcao = input(FRENTE_MAGENTA_CLARO + ESTILO_NEGRITO + "\nOpção: " + RESET).strip()

        if sub_opcao == "1":
            print(FRENTE_AMARELO_CLARO + ESTILO_NEGRITO + "\n--- SOMA EM LOTE ---" + RESET)
            lista = coletar_lista_numeros()
            if lista:
                resultado = formatar_numero(somarmultiplosnumeros(lista))
                exibir_mensagem(f"Soma de {lista} = {resultado}", FRENTE_VERDE_CLARO)
            else:
                exibir_mensagem("Lista vazia. Nenhum cálculo realizado.", FRENTE_VERMELHO_CLARO)
            input(FRENTE_CINZA + "\nPressione ENTER para continuar..." + RESET)

        elif sub_opcao == "2":
            print(FRENTE_AMARELO_CLARO + ESTILO_NEGRITO + "\n--- MULTIPLICAÇÃO EM LOTE ---" + RESET)
            lista = coletar_lista_numeros()
            if lista:
                resultado = formatar_numero(multiplicarmultiplosnumeros(lista))
                exibir_mensagem(f"Produto de {lista} = {resultado}", FRENTE_VERDE_CLARO)
            else:
                exibir_mensagem("Lista vazia. Nenhum cálculo realizado.", FRENTE_VERMELHO_CLARO)
            input(FRENTE_CINZA + "\nPressione ENTER para continuar..." + RESET)

        elif sub_opcao == "3":
            break
        else:
            exibir_mensagem("Opção inválida. Tente novamente.", FRENTE_VERMELHO_CLARO)
            input(FRENTE_CINZA + "\nPressione ENTER para continuar..." + RESET)

def tela_verificacoes():
    while True:
        limpar_tela()
        borda = FRENTE_VERDE_CLARO + ESTILO_NEGRITO
        txt = FRENTE_BRANCO_CLARO
        num = FRENTE_AMARELO_CLARO + ESTILO_NEGRITO

        print(f"{borda}╔══════════════════════════════════════╗{RESET}")
        print(f"{borda}║       VERIFICAÇÕES NUMÉRICAS         ║{RESET}")
        print(f"{borda}╠══════════════════════════════════════╣{RESET}")
        print(f"{borda}║ {num}1.{RESET} {txt}Verificar se é PAR                {borda}║{RESET}")
        print(f"{borda}║ {num}2.{RESET} {txt}Verificar se é INTEIRO            {borda}║{RESET}")
        print(f"{borda}║ {num}3.{RESET} {txt}Voltar ao menu principal          {borda}║{RESET}")
        print(f"{borda}╚══════════════════════════════════════╝{RESET}")

        sub_opcao = input(FRENTE_MAGENTA_CLARO + ESTILO_NEGRITO + "\nOpção: " + RESET).strip()

        if sub_opcao == "1":
            print(FRENTE_AMARELO_CLARO + ESTILO_NEGRITO + "\n--- VERIFICAR PARIDADE ---" + RESET)
            num_input = coletar_unico_numero("Digite um número: ")
            
            if not ehinteiro(num_input):
                exibir_mensagem(f"O número {num_input} é decimal (apenas inteiros são pares/ímpares).", FRENTE_AMARELO_CLARO)
            elif ehpar(num_input):
                exibir_mensagem(f"O número {num_input} é PAR.", FRENTE_VERDE_CLARO)
            else:
                exibir_mensagem(f"O número {num_input} é ÍMPAR.", FRENTE_CIANO_CLARO)
            input(FRENTE_CINZA + "\nPressione ENTER para continuar..." + RESET)

        elif sub_opcao == "2":
            print(FRENTE_AMARELO_CLARO + ESTILO_NEGRITO + "\n--- VERIFICAR SE É INTEIRO ---" + RESET)
            num_input = coletar_unico_numero("Digite um número: ")
            
            if ehinteiro(num_input):
                exibir_mensagem(f"O número {num_input} é INTEIRO.", FRENTE_VERDE_CLARO)
            else:
                exibir_mensagem(f"O número {num_input} é DECIMAL/FLOAT.", FRENTE_AMARELO_CLARO)
            input(FRENTE_CINZA + "\nPressione ENTER para continuar..." + RESET)

        elif sub_opcao == "3":
            break
        else:
            exibir_mensagem("Opção inválida. Tente novamente.", FRENTE_VERMELHO_CLARO)
            input(FRENTE_CINZA + "\nPressione ENTER para continuar..." + RESET)

def menu_principal():
    limpar_tela()
    borda = FRENTE_AMARELO_CLARO + ESTILO_NEGRITO
    txt = FRENTE_BRANCO_CLARO
    num = FRENTE_CIANO_CLARO + ESTILO_NEGRITO

    print(f"{borda}╔══════════════════════════════════════╗{RESET}")
    print(f"{borda}║         CALCULADORA AVANÇADA         ║{RESET}")
    print(f"{borda}╠══════════════════════════════════════╣{RESET}")
    print(f"{borda}║ {num}1.{RESET} {txt}Operações em Lote (Listas)        {borda}║{RESET}")
    print(f"{borda}║ {num}2.{RESET} {txt}Verificações (Par/Inteiro)        {borda}║{RESET}")
    print(f"{borda}║ {num}3.{RESET} {txt}Sair                              {borda}║{RESET}")
    print(f"{borda}╚══════════════════════════════════════╝{RESET}")

while True:
    menu_principal()
    opcao = input(FRENTE_MAGENTA_CLARO + ESTILO_NEGRITO + "\nEscolha uma tela: " + RESET).strip()

    if opcao == "1":
        tela_operacoes_lote()
    elif opcao == "2":
        tela_verificacoes()
    elif opcao == "3":
        exibir_mensagem("Encerrando a calculadora...", FRENTE_AZUL_CLARO)
        break
    else:
        exibir_mensagem("Opção inválida. Tente novamente.", FRENTE_VERMELHO_CLARO)
        input(FRENTE_CINZA + "\nPressione ENTER para continuar..." + RESET)
