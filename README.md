# 📌 Nome do Projeto

**Exercícios com PySpark — Análise de Dados em IoT**

---

## ✍️ Autor

**Caio Pereira De Paula** — RA: 79630

**Victor Milu** — RA: 51917

**Igor Alves Cardoso** — RA: 79630

---

## 📘 Descrição

Este projeto consiste em uma série de exercícios utilizando **Apache Spark com PySpark** para realizar leitura, transformação, análise e exportação de dados, voltado ao contexto de **IoT (Internet das Coisas)**.

Também foi incluída uma **pesquisa técnica** sobre **Edge Computing** e **Progressive Web Apps (PWAs)**, com comparações e aplicações práticas.

---

## 📁 Estrutura do Projeto

```
Exercicio_IOT/
│
├── dados.csv                      # Dados utilizados nos exercícios 1 a 5
├── dados.json                     # Dados em formato JSON (exercício 5)
├── vendas.csv                     # Dados simulados de vendas (exercício 6)
├── exercicio1.py                  # Filtros com PySpark
├── exercicio2.py                  # Seleções, ordenações e transformação de dados
├── exercicio3.py                  # Agregações e agrupamentos
├── exercicio4.py                  # Consultas com Spark SQL
├── exercicio5.py                  # Leitura JSON e escrita em Parquet
├── exerciciofinal6.py            # Análise de vendas e exportação em CSV
├── pesquisa_edge_pwa.pdf         # Pesquisa sobre Edge Computing e PWAs
└── README.md                      # Este arquivo
```

---

## 🛠️ Tecnologias Utilizadas

- Python 3.10
- Apache Spark 3.5.5
- PySpark
- JDK 11 (Adoptium)
- VSCode
- PowerShell / CMD (Windows)
- Git + GitHub

---

## ⚙️ Pré-requisitos

Para executar o projeto localmente:

1. Ter o [Python 3.10](https://www.python.org/downloads/release/python-31012/) instalado.
2. Ter o [Java JDK 11](https://adoptium.net/pt/temurin/releases/?version=11) instalado e configurado no `JAVA_HOME`.
3. Criar e ativar um ambiente virtual:

```bash
python -m venv venv
.env\Scriptsctivate
```

4. Instalar dependências:

```bash
pip install pyspark
```

---

## ▶️ Executando os Arquivos

Com o ambiente ativado, você pode executar qualquer um dos scripts:

```bash
python exercicio1.py
```

Para o desafio final (vendas):

```bash
python exerciciofinal6.py
```

