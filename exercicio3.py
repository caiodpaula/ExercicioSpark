import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

# Configurações do ambiente (ajuste conforme necessário)
os.environ["PYSPARK_PYTHON"] = "C:/Users/caiod/OneDrive/Área de Trabalho/Exercicio_IOT/venv/Scripts/python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/caiod/OneDrive/Área de Trabalho/Exercicio_IOT/venv/Scripts/python.exe"

# Criar SparkSession
spark = SparkSession.builder.appName("Exercicio3").getOrCreate()

# Carregar o CSV
df = spark.read.csv("dados.csv", header=True, inferSchema=True)

# Mostrar o schema para garantir que "idade" é um número
print("▶ Esquema:")
df.printSchema()

# Calcular a idade média
print("\n▶ Idade média:")
df.agg(avg("idade").alias("idade_media")).show()

# Contar número de pessoas por cidade
print("\n▶ Número de pessoas por cidade:")
df.groupBy("cidade").count().show()

# Finalizar sessão
spark.stop()
