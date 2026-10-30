# Projeto 5 — Calculadora Aprimorada

<div align="center"><img src="https://i.imgur.com/QsU3CUo.png" title="source: imgur.com" width="50%"/></div>

> Construa uma calculadora nova e melhor, feita de funções que trabalham com vários números de uma vez.

| | |
|---|---|
| **Tema** | Algoritmos |
| **Nível** | Iniciante |
| **Tempo sugerido** | 40 minutos |
| **O que você vai praticar** | Funções, fluxo de controle, ordem das operações (BODMAS) e tipos de números |

---

## Contexto

Na primeira calculadora, cada conta envolvia **dois** números. Uma calculadora melhorada precisa ir além: somar ou multiplicar uma lista inteira de números e responder a perguntas simples sobre eles, como "este número é par?".

Em vez de um programa único, você vai criar **funções**: pequenos blocos de código, cada um com uma tarefa bem definida, que podem ser usados quantas vezes você quiser. É assim que calculadoras e programas de verdade são construídos.

**Importante:** crie uma calculadora **nova, do zero**, em vez de atualizar a primeira que você criou. Mas leve com você o que aprendeu sobre **fluxo de controle**, **ordem das operações (BODMAS)** e **funções**.

## O que você deve criar

Crie, no arquivo `main.py`, as quatro funções abaixo. **Os nomes precisam ser exatamente estes**, pois os testes vão procurar por eles.

| Função | Recebe | Devolve |
|---|---|---|
| `somarmultiplosnumeros` | uma **lista** de números: `[num, num, ...]` | a **soma** desses números |
| `multiplicarmultiplosnumeros` | uma **lista** de números: `[num, num, ...]` | o **produto** desses números, multiplicando cada número pelo próximo |
| `ehpar` | **um** número | `True` se o número for **par e inteiro**, ou `False` se não for |
| `ehinteiro` | **um** número | `True` se o número for **inteiro**, ou `False` se não for |

### Sobre os números

As listas podem conter números **inteiros**, **decimais** e **negativos**, misturados. Nos nomes dos testes, essas listas aparecem como "números complexos".

### Sobre números pares

Um número é par quando é **inteiro** e pode ser dividido por 2 **sem sobrar resto**. Por isso, números com parte decimal, como `-3.8`, **nunca** são pares.

## Exemplos

| Chamada | A função devolve |
|---|---|
| `somarmultiplosnumeros([5, 10, 15])` | `30` |
| `somarmultiplosnumeros([0.5, -4, 2])` | `-1.5` |
| `multiplicarmultiplosnumeros([2, 5])` | `10` |
| `multiplicarmultiplosnumeros([-1, 3, 2.5])` | `-7.5` |
| `ehpar(8)` | `True` |
| `ehpar(5)` | `False` |
| `ehpar(2.5)` | `False` |
| `ehinteiro(10)` | `True` |
| `ehinteiro(-6)` | `True` |
| `ehinteiro(4.2)` | `False` |

## Veja as suas funções funcionando

Os testes conferem as suas funções, mas você também pode **vê-las em ação**. No final do `main.py`, depois das funções, escreva algumas listas de números e exiba o que cada função devolve.

Por exemplo, monte uma lista com os números que quiser, peça a soma e a multiplicação dela e mostre o resultado na tela. Depois, escolha um número e veja se ele é par e se é inteiro.

Assim, ao rodar o `main.py`, você enxerga o resultado de cada função sem precisar digitar nada.

## Antes de programar

Pense em cada função separadamente, no papel:

- Se você tivesse que somar uma lista de números à mão, como faria? E se a lista tivesse 3 números? E 300?
- Qual é o "ponto de partida" certo para uma soma? E para uma multiplicação?
- Como você descobriria, só olhando para um número, se ele tem parte decimal?

## Pontos de atenção

- **Os nomes das funções importam.** Escreva exatamente `somarmultiplosnumeros`, `multiplicarmultiplosnumeros`, `ehpar` e `ehinteiro`, em letras minúsculas, sem acentos e sem espaços.
- **As funções devolvem o valor** (não o exibem na tela). Os testes vão usar o que elas devolverem.
- **Não use `input()` no `main.py`.** Os testes abrem o seu arquivo, e um programa esperando uma resposta do usuário travaria os testes. Listas escritas no próprio código e `print` podem ser usados à vontade.
- **Cada função tem uma tarefa só.** Não misture, por exemplo, a soma com a verificação de par.
- **Maiúsculas e minúsculas contam.** `True` e `False` começam com letra maiúscula.

> **Lembre-se:** este projeto é corrigido automaticamente, e computadores são muito literais.