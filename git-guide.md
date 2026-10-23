```markdown
# Guia Rápido de Git e GitHub

## 1. Configuração Inicial

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
git config --global init.defaultBranch main
git config --global core.editor "code --wait"   # ou nano/vim
```

Verificar:
```bash
git config --list
```

## 2. Inicialização

### Novo repositório local
```bash
git init
git add .
git commit -m "Initial commit"
```

### Clonar repositório existente
```bash
git clone https://github.com/usuario/repositorio.git
cd repositorio
```

### Conectar ao GitHub
```bash
git remote add origin https://github.com/usuario/repositorio.git
git push -u origin main
```

## 3. Fluxo de Desenvolvimento

```bash
# Atualizar branch
git pull

# Criar e mudar para nova branch
git checkout -b feature/nome-da-feature

# Ver status e diferenças
git status
git diff

# Adicionar arquivos
git add arquivo.js          # específico
git add .                   # todos

# Commit
git commit -m "mensagem clara"

# Enviar para o remoto
git push -u origin feature/nome-da-feature

# Voltar para main e atualizar
git checkout main
git pull
```

### Comandos úteis
```bash
git log --oneline           # histórico resumido
git branch -d nome-branch   # apagar branch local
git stash                   # guardar alterações temporárias
git stash pop               # recuperar
```

## 4. Boas Práticas de Commits

### Formato recomendado (Conventional Commits)
```
tipo(escopo): descrição curta

[corpo opcional]
```

**Tipos comuns:**
- `feat`: nova funcionalidade
- `fix`: correção de bug
- `docs`: documentação
- `style`: formatação (sem mudança de código)
- `refactor`: refatoração
- `test`: testes
- `chore`: tarefas de manutenção

### Exemplos bons
```
feat(auth): adiciona login com Google
fix(api): corrige erro 500 no endpoint de usuários
docs: atualiza README com instruções de instalação
```

### Regras
- Mensagem no imperativo (“adiciona”, não “adicionou”)
- Máximo ~50 caracteres na primeira linha
- Uma responsabilidade por commit
- Não commitar código quebrado ou arquivos sensíveis (`.env`, senhas)
- Use `.gitignore` sempre

### Exemplo de `.gitignore` básico
```
node_modules/
.env
dist/
*.log
.DS_Store
```

---

**Dica final:** Prefira branches pequenas, commits frequentes e PRs claros.