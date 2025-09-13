import pandas as pd
from pathlib import Path


base = Path("1_projeto_basico_relatorio_vendas")
clientes_path = base / "clientes.csv"
vendas_path = base / "vendas.csv"

df_clientes = pd.read_csv(clientes_path)
df_vendas = pd.read_csv(vendas_path)

df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'], errors='coerce')

df_vendas['ano_mes'] = df_vendas['data_venda'].dt.to_period('M').astype(str)

df = df_vendas.merge(df_clientes, on='id_cliente', how='left')

vendas_por_cliente = df.groupby(['id_cliente','nome'])['valor_venda'] \
                        .agg(qtd_vendas='count', total_gasto='sum', ticket_medio='mean') \
                        .reset_index()

vendas_por_mes = df.groupby('ano_mes')['valor_venda'] \
                   .agg(qtd_vendas='count', total_receita='sum', ticket_medio='mean') \
                   .reset_index()

out_dir = Path("relatorio_saida")
out_dir.mkdir(exist_ok=True)

vendas_por_cliente.to_csv(out_dir / "vendas_por_cliente.csv", index=False)
vendas_por_mes.to_csv(out_dir / "vendas_por_mes.csv", index=False)
df.to_csv(out_dir / "vendas_com_clientes.csv", index=False)

md = []
md.append("# Relatório de Vendas\n")
md.append(f"- Total de vendas: {len(df)}\n")
md.append(f"- Total de receita: R$ {df['valor_venda'].sum():,.2f}\n\n")
md.append("## Top clientes\n")
md.append(vendas_por_cliente.sort_values('total_gasto', ascending=False).to_markdown(index=False))
with open(out_dir / "relatorio_vendas.md", "w", encoding="utf-8") as f:
    f.write("\n".join(md))

with pd.ExcelWriter(out_dir / "relatorio_vendas.xlsx") as writer:
    vendas_por_cliente.to_excel(writer, sheet_name="vendas_por_cliente", index=False)
    vendas_por_mes.to_excel(writer, sheet_name="vendas_por_mes", index=False)
    df.to_excel(writer, sheet_name="vendas_com_clientes", index=False)
