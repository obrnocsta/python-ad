import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

perguntas = [
    "Nome", "Profissão/Formação", "Primeiro Adjetivo", 
    "Segundo Adjetivo", "Primeira Comida", "Segunda Comida/Bebida", "Sentimento"
]

respostas = []

for item in perguntas:
    limpar_tela()
    print("--- Jogo do Texto Maluco (Generation Brasil) ---\n")
    resposta = input(f"Digite um(a) {item}: ")
    respostas.append(resposta)

limpar_tela()

historia = """
{} começou hoje o seu primeiro curso na Generation Brasil.
Está cursando a formação em {}.
Achou a sua turma muito {} mas o instrutor era, no mínimo, {}.
No almoço, comeu {} e {} enquanto revisava as suas anotações.
Ao final do dia, sente-se {}, mas tem a determinação de concluir a jornada.
""".format(*respostas)

print("--- História ---")
print(historia)
