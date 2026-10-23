perguntas = [
    "Nome",
    "Profissão/Formação",
    "Primeiro Adjetivo (para a turma)",
    "Segundo Adjetivo (para o instrutor)",
    "Primeira Comida",
    "Segunda Comida/Bebida",
    "Um Sentimento"
]

respostas = []

print("--- Jogo do Texto Maluco (Generation Brasil) ---\n")

for item in perguntas:
    resposta = input(f"Digite um(a) {item}: ")
    respostas.append(resposta)

historia = (
    f"\n{respostas[0]} começou hoje o seu primeiro curso na Generation Brasil.\n"
    f"Está cursando a formação em {respostas[1]}.\n"
    f"Achou a sua turma muito {respostas[2]} mas o instrutor era, no mínimo, {respostas[3]}.\n"
    f"No almoço, comeu {respostas[4]} e {respostas[5]} enquanto revisava as suas anotações.\n"
    f"Ao final do dia, sente-se {respostas[6]}, mas tem a determinação de concluir a jornada."
)

print("\n--- História ---")
print(historia)
