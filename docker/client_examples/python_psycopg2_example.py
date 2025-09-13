import os
import psycopg2

# Use variáveis de ambiente se existirem, senão defaults do compose
HOST = os.getenv("PGHOST", "localhost")
PORT = int(os.getenv("PGPORT", "5432"))
USER = os.getenv("PGUSER", "desafio")
PASSWORD = os.getenv("PGPASSWORD", "desafio123")
DB = os.getenv("PGDATABASE", "desafio_db")

conn_str = f"host={HOST} port={PORT} dbname={DB} user={USER} password={PASSWORD}"

def main():
    print("Conectando em:", conn_str.replace(PASSWORD, "***"))
    with psycopg2.connect(conn_str) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT current_database(), current_user;")
            print("DB/User:", cur.fetchone())

            cur.execute("SELECT schema_name FROM information_schema.schemata WHERE schema_name in ('basic','logs','licitacao') ORDER BY 1;")
            print("Schemas:", [r[0] for r in cur.fetchall()])

            cur.execute("SELECT count(*) FROM information_schema.tables WHERE table_schema in ('basic','logs','licitacao');")
            print("Tabelas totais:", cur.fetchone()[0])

            # Exemplos de queries
            cur.execute("SELECT * FROM information_schema.tables WHERE table_schema='basic' ORDER BY table_name;")
            print("basic:", [r[2] for r in cur.fetchall()])

if __name__ == "__main__":
    main()
