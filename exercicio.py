import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Corrigir caminho do Python para ambiente virtual (ajuste se necessário)
os.environ["PYSPARK_PYTHON"] = "C:/Users/caiod/OneDrive/Área de Trabalho/Exercicio_IOT/venv/Scripts/python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/caiod/OneDrive/Área de Trabalho/Exercicio_IOT/venv/Scripts/python.exe"

# Criar SparkSession
spark = SparkSession.builder.appName("Exercicio1").getOrCreate()

# Carregar o CSV com opções extras
df = spark.read.csv(
    "dados.csv",
    header=True,
    inferSchema=True,
    sep=",",              # garante separador correto
    encoding="utf-8"      # evita erro com acentos
)

# Mostrar o schema detectado (debug útil)
print("▶ Esquema detectado pelo Spark:")
df.printSchema()

# Exibir as primeiras 5 linhas
print("▶ Primeiras 5 linhas do DataFrame:")
df.show(5)

# Filtrar pessoas com idade acima de 25
print("▶ Pessoas com idade acima de 25:")
df.filter(col("idade") > 25).show()

# Finalizar a SparkSession
spark.stop()
