import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper

# Configurar ambiente do Python
os.environ["PYSPARK_PYTHON"] = "C:/Users/caiod/OneDrive/Área de Trabalho/Exercicio_IOT/venv/Scripts/python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/caiod/OneDrive/Área de Trabalho/Exercicio_IOT/venv/Scripts/python.exe"

# Criar SparkSession
spark = SparkSession.builder.appName("Exercicio2").getOrCreate()

# Carregar CSV
df = spark.read.csv("dados.csv", header=True, inferSchema=True)

# ▶ Apenas colunas nome e cidade
df_selecionado = df.select("nome", "cidade")
print("▶ Apenas colunas nome e cidade:")
df_selecionado.show()

# ▶ Ordenado pela idade (decrescente)
df_ordenado = df.orderBy(col("idade").desc())
print("▶ Ordenado pela idade (decrescente):")
df_ordenado.show()

# ▶ Nomes em letras maiúsculas
df_maiusculo = df.withColumn("nome", upper(col("nome")))
print("▶ Nomes em letras maiúsculas:")
df_maiusculo.show()

# Encerrar a sessão
spark.stop()
