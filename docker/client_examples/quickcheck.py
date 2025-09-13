
# Executa verificações rápidas via psql dentro do container
# Uso: python quickcheck.py

import subprocess, os, sys

container = "desafio_postgres"

def run(cmd):
    print("$", " ".join(cmd))
    res = subprocess.run(cmd, text=True, capture_output=True)
    print(res.stdout)
    if res.returncode != 0:
        print(res.stderr, file=sys.stderr)
    return res.returncode

def main():
    # Mostra serviços
    run(["docker", "compose", "ps"])
    # Checa conexão e schemas
    run(["docker", "exec", "-i", container,
         "psql", "-U", "desafio", "-d", "desafio_db",
         "-c", "SELECT version();"])
    run(["docker", "exec", "-i", container,
         "psql", "-U", "desafio", "-d", "desafio_db",
         "-c", "SELECT schema_name FROM information_schema.schemata WHERE schema_name in ('basic','logs','licitacao') ORDER BY 1;"])

if __name__ == "__main__":
    sys.exit(main())
