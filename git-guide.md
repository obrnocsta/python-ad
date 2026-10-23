
**Guia Rápido de Git: Comandos Essenciais, Boas Práticas e Soluções**

Este guia prático reúne os passos iniciais de configuração, comandos mais utilizados no dia a dia com o Git, boas práticas para manter seu histórico limpo e as soluções para os problemas mais comuns.

1. Configuração Inicial e Boas Práticas

Antes de criar seu primeiro commit, é fundamental configurar sua identidade. O Git anexa essas informações a cada commit que você faz para que as pessoas saibam quem escreveu o código.

Configurando o Git pela primeira vez

Abra o seu terminal e execute os comandos abaixo substituindo pelos seus dados:
bash
# Define o seu nome de usuário globalmente
git config --global user.name "Seu Nome Completo"

# Define o seu e-mail globalmente (use o mesmo e-mail da sua conta do GitHub/GitLab)
git config --global user.email "seu@email.com"

# [Recomendável] Define a branch padrão para 'main' (o padrão antigo era 'master')
git config --global init.defaultBranch main

# [Recomendável] Ativa o realce de cores no terminal para facilitar a leitura
git config --global color.ui auto
Use o código com cuidado.
Para verificar se as configurações foram salvas corretamente, você pode listar as configurações ativas com o comando git config --list.

Boas Práticas Iniciais para Commits

Um bom histórico de commits funciona como uma linha do tempo clara do projeto. Siga estas regras simples desde o início:
• Faça commits atômicos: Prefira fazer commits pequenos e frequentes que resolvam apenas uma tarefa específica, em vez de um único commit gigante com várias alterações misturadas.
• Use o modo imperativo na mensagem: Escreva a mensagem como se estivesse dando uma ordem ao Git (ex: Adiciona componente de botão em vez de Adicionado botão ou Adicionando botão).
• Seja claro e conciso: A primeira linha da mensagem de commit deve ser curta (máximo de 50 caracteres) e resumir diretamente o que foi feito.
• Nunca comite arquivos desnecessários: Arquivos de configuração local, senhas, chaves de API e pastas de dependências (como a node_modules) nunca devem ser commitados. Use sempre um arquivo .gitignore na raiz do projeto para ignorá-los automaticamente.

2. Comandos Essenciais


Criação e Clonagem de Repositórios

• git init — Inicializa um novo repositório Git no diretório atual.
• git clone <URL> — Cria uma cópia local de um repositório remoto existente.

Fluxo de Trabalho Básico (Staging e Commit)

• git status — Mostra o estado atual do repositório e quais arquivos foram modificados.
• git add . — Adiciona todas as alterações da pasta atual à área de preparação (staging).
• git commit -m "mensagem" — Salva as alterações preparadas no histórico local seguindo as boas práticas.
• git log — Exibe o histórico de commits do repositório.
• git diff — Mostra as diferenças nos arquivos que ainda não foram preparados.

Trabalho com Branches

• git branch — Lista todas as branches locais.
• git switch -c <nome> — Cria e muda para uma nova branch.
• git switch <nome> — Alterna para uma branch existente.
• git merge <branch> — Mescla a branch especificada na branch atual.
• git branch -d <nome> — Deleta uma branch local de forma segura (já mesclada).
• git branch -D <nome> — Força a exclusão de uma branch local (mesmo com alterações não salvas).

Sincronização Remota

• git fetch — Baixa as atualizações do servidor remoto sem alterar seu código local.
• git pull — Baixa e integra as alterações do repositório remoto na branch atual.
• git push origin <nome-da-branch> — Envia os commits locais para o repositório remoto.
• git push origin --delete <nome-da-branch> — Deleta a branch diretamente no repositório remoto.

3. Problemas Comuns e Como Resolver


Errei a mensagem do último commit (local)

• Solução: git commit --amend -m "Nova mensagem corrigida"

Adicionei um arquivo por engano no git add

• Solução: git restore --staged <nome-do-arquivo>
(O arquivo sai da fila de commit, mas mantém suas alterações intactas na máquina).

Commitei na branch errada (ex: na main em vez de uma nova branch)

• Solução:bash
git branch <nome-da-nova-branch>
git reset HEAD~1 --soft
git switch <nome-da-nova-branch>
Use o código com cuidado.

Quero descartar todas as alterações locais e voltar ao último commit

• Solução: git reset --hard HEAD
(Atenção: Comando destrutivo. Apaga permanentemente tudo o que não foi commitado).

Conflito de Merge (Merge Conflicts)

• Solução:
	1. Identifique os arquivos conflitantes com git status.
	2. Abra os arquivos no editor de código e limpe as marcações (<<<<<<<, =======, >>>>>>>).
	3. Escolha qual trecho de código deve ser mantido.
	4. Salve o arquivo e finalize com o comando abaixo:bash
git add <arquivo-corrigido>
git commit -m "Resolve conflito de merge"
Use o código com cuidado.
Se quiser, eu posso gerar o arquivo guia-git.md pronto para você baixar ou posso te mostrar exemplos de como estruturar um arquivo .gitignore padrão para o seu tipo de projeto. O que prefere?
