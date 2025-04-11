import os
from pyspark.sql import SparkSession

# Variáveis de ambiente
os.environ["PYSPARK_PYTHON"] = "C:/Users/caiod/OneDrive/Área de Trabalho/Exercicio_IOT/venv/Scripts/python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/caiod/OneDrive/Área de Trabalho/Exercicio_IOT/venv/Scripts/python.exe"
os.environ["HADOOP_HOME"] = "C:/hadoop"

# Criar SparkSession
spark = SparkSession.builder.appName("Exercicio5_IO").getOrCreate()

# Leitura de JSON (corrigido)
df_json = spark.read.option("multiLine", True).json("dados.json")

print("▶ Dados lidos do JSON:")
df_json.show()

# Filtrar
df_filtrado = df_json.filter(df_json.idade > 30)

# Salvar como Parquet
df_filtrado.write.mode("overwrite").parquet("saida_parquet")

print("▶ Dados filtrados salvos em formato Parquet.")

spark.stop()
