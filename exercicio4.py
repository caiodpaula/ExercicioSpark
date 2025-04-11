import os
from pyspark.sql import SparkSession

# Caminho do Python do venv
os.environ["PYSPARK_PYTHON"] = "C:/Users/caiod/OneDrive/Área de Trabalho/Exercicio_IOT/venv/Scripts/python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = "C:/Users/caiod/OneDrive/Área de Trabalho/Exercicio_IOT/venv/Scripts/python.exe"

# Criar SparkSession
spark = SparkSession.builder.appName("Exercicio4_SQL").getOrCreate()

# Ler CSV
df = spark.read.csv("dados.csv", header=True, inferSchema=True)

# Registrar o DataFrame como uma tabela temporária
df.createOrReplaceTempView("tabela_pessoas")

# Consultar pessoas de uma cidade específica
cidade_especifica = "São Paulo"
consulta_cidade = f"""
    SELECT * FROM tabela_pessoas
    WHERE cidade = '{cidade_especifica}'
"""
pessoas_na_cidade = spark.sql(consulta_cidade)
print(f"▶ Pessoas que moram em '{cidade_especifica}':")
pessoas_na_cidade.show()

# Consulta para soma das idades
consulta_soma_idades = """
    SELECT SUM(idade) AS soma_das_idades
    FROM tabela_pessoas
"""
soma_idades = spark.sql(consulta_soma_idades)
print("▶ Soma das idades:")
soma_idades.show()

# Finalizar
spark.stop()
