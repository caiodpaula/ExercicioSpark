import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, year, desc

# Configuração de ambiente (ajuste se necessário)
os.environ["PYSPARK_PYTHON"] = "C:/Users/caiod/OneDrive/Área de Trabalho/Exercicio_IOT/venv/Scripts/python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/caiod/OneDrive/Área de Trabalho/Exercicio_IOT/venv/Scripts/python.exe"

# Criar SparkSession
spark = SparkSession.builder.appName("DesafioFinal").getOrCreate()

# Criar DataFrame com dados fictícios
dados = [
    (1, 250.0, "2022-01-10"),
    (2, 400.0, "2022-06-15"),
    (3, 150.0, "2023-03-12"),
    (1, 300.0, "2023-07-19"),
    (2, 500.0, "2024-02-01"),
]

colunas = ["id_cliente", "valor_compra", "data_compra"]

df = spark.createDataFrame(dados, colunas)

# Mostrar os dados
print("▶ Dados de vendas:")
df.show()

# Clientes com maior valor de compra
print("▶ Maiores compras:")
df.orderBy(desc("valor_compra")).show(3)

# Agrupar por ano e somar valores
print("▶ Total de vendas por ano:")
df_com_ano = df.withColumn("ano", year("data_compra"))
df_ano = df_com_ano.groupBy("ano").sum("valor_compra").withColumnRenamed("sum(valor_compra)", "total_vendas")
df_ano.show()

# Salvar resultado como CSV
df_ano.write.mode("overwrite").csv("vendas_por_ano")

# Encerrar sessão
spark.stop()
