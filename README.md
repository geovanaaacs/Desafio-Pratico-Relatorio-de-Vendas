# Relatório de Vendas – Projeto de Estudo

Este projeto é a solução para um desafio técnico que consiste em construir um pipeline de dados simples. O script principal, `gerar_relatorio.py`, automatiza o processo de extração, transformação e carregamento (ETL) de dados de vendas e clientes, gerando um conjunto de relatórios analíticos em múltiplos formatos.

## 📝 O que é o projeto

O script principal `gerar_relatorio.py` lê dois arquivos `.csv` (`clientes.csv` e `vendas.csv`), faz algumas limpezas, cria novas colunas (tipo `ano_mes`) e calcula métricas simples.

Depois ele salva tudo em uma pasta chamada `relatorio_saida`, que já sai com:
- CSVs prontos com as análises.
- Um arquivo Excel com várias abas.
- Um mini-relatório em Markdown com indicadores principais.

## ✔️ Funcionalidades

- **Leitura dos dados**: Importa os dois CSVs de clientes e vendas.
- **Tratamento básico**: Ajusta datas e tipos de dados para não dar erro.
- **Junção e criação de coluna `ano_mes`**: Para analisar por período.
- **Agrupamentos**:
  - **Por cliente**: Quantidade de vendas, total gasto e ticket médio.
  - **Por mês**: Total de vendas, receita e ticket médio.
- **Saída em vários formatos**: CSV, Excel e um resumo em Markdown.

## 💻 Tecnologias

- **Python 3**
- **Bibliotecas**:
  - **pandas** para toda a parte de análise.
  - **pathlib** para lidar com caminhos de arquivos.

## 🚀 Como rodar

1.  Tenha o **Python 3** instalado.

2.  Clone o repositório e acesse a pasta:
    ```bash
    git clone [https://github.com/geovanaaacs/Desafio-Pratico-Relatorio-de-Vendas.git](https://github.com/geovanaaacs/Desafio-Pratico-Relatorio-de-Vendas.git)
    cd Desafio-Pratico-Relatorio-de-Vendas
    ```

3.  Instale a dependência principal:
    ```bash
    pip install pandas
    ```

4.  Execute o script:
    ```bash
    python 1_projeto_basico_relatorio_vendas/gerar_relatorio.py
    ```
Uma pasta `relatorio_saida` vai aparecer com todos os arquivos de resultado.

## 📊 Saídas geradas

- CSV por cliente (`vendas_por_cliente.csv`)
- CSV por mês (`vendas_por_mes.csv`)
- Excel com abas para cada análise
- Markdown com um resumo rápido

## 👩‍💻 Sobre mim

Projeto feito por **Geovana**, como parte dos meus estudos em Python e análise de dados.
