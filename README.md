# Agenda Amiga API

A *Agenda Amiga API* é uma interface REST desenvolvida com Flask para gerenciar compromissos de forma simples e eficiente. Perfeita para sistemas que exigem operações básicas como criar, listar, atualizar e remover compromissos.

## Funcionalidades

* Criar novos compromissos
* Listar todos os compromissos
* Atualizar compromissos existentes
* Remover compromissos

## Tecnologias Utilizadas

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Migrate
* Alembic
* PostgreSQL

## Estrutura de Pastas

```bash
.
├── app/
│   ├── controllers/         # Lógica dos endpoints
│   ├── models/              # Modelos de dados
│   ├── schemas/             # Validação e serialização
│   ├── services/            # Regras de negócio
│   ├── __init__.py
│   └── config.py            # Configurações da aplicação
├── migrations/              # Arquivos de migração do banco
├── .gitignore
├── main.py                  # Ponto de entrada da aplicação
└── requirements.txt         # Dependências do projeto
```

## Como Rodar Localmente

```bash
# Clone o repositório
git clone https://github.com/Ivysonin/Agenda-Amiga_API.git

# Acesse a pasta do projeto
cd Agenda-Amiga_API

# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual (Windows)
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
SECRET_KEY='chave-secreta-aqui'
DATABASE_URL='postgresql://usuário:senha@host:porta/nome_do_banco'

# Execute as migrações
flask db init
flask db migrate
flask db upgrade

# Rode a aplicação
python main.py
```

## 📄 Licença

Este projeto está licenciado sob os termos da [Licença MIT](./LICENSE).
