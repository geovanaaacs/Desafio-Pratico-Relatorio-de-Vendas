
# Docker - Postgres para os Desafios

## Pré-requisitos
- Docker e Docker Compose Plugin instalados.

## Como subir o banco
1) Dentro da pasta `docker/`, crie o `.env` (opcional):  
   ```bash
   cp .env.example .env
   ```
2) Suba os serviços:
   ```bash
   docker compose up -d
   ```
3) Aguarde o `db` ficar saudável (**healthy**). Verifique com:
   ```bash
   docker compose ps
   ```

## O que já vem pronto
- Postgres 16 acessível em `localhost:5432`
- Usuário/Senha padrão: `desafio/desafio123`
- Banco padrão: `desafio_db`
- **Schemas** criados: `basic`, `logs`, `licitacao`
- Tabelas de cada projeto criadas automaticamente na **primeira inicialização**.

> Observação: os scripts em `init/` só rodam automaticamente **na primeira vez** que o volume do Postgres é criado.

## Conexão
- String (psycopg2):
  ```
  postgresql://desafio:desafio123@localhost:5432/desafio_db
  ```
- SQLAlchemy:
  ```python
  create_engine("postgresql+psycopg2://desafio:desafio123@localhost:5432/desafio_db")
  ```

## pgAdmin (opcional)
- Acesse: `http://localhost:5050`
- Login: o que está no `.env` (default `admin@example.com` / `admin123`)
- Crie um **Server** apontando para:
  - Host: `db` (de dentro do pgAdmin container) **ou** `host.docker.internal`/`localhost` (se preferir)
  - Port: `5432`
  - User: `desafio`
  - Password: `desafio123`
  - Database: `desafio_db`

## Rodar scripts manualmente (se precisar)
Você pode reexecutar qualquer script SQL dentro do container:
```bash
docker exec -i desafio_postgres psql -U desafio -d desafio_db -v ON_ERROR_STOP=1 -f /docker-entrypoint-initdb.d/01_basic.sql
```

## Resetar o banco (cuidado!)
Para apagar os dados e recriar tudo do zero (isso **apaga o volume**):
```bash
docker compose down -v
docker compose up -d
```

## Schemas e tabelas criados
- Schema `basic`: `clientes`, `vendas`
- Schema `logs`: `logs`
- Schema `licitacao`: `pregao`, `empresa`, `item`, `proposta`

> Se você executar os `init.sql` dentro de cada projeto manualmente, as tabelas serão criadas no schema `public`. No Docker, criamos schemas separados para evitar conflitos.
