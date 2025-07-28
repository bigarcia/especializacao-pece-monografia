from pyspark.sql import SparkSession

# Cria sessão Spark
spark = SparkSession.builder \
    .appName("Credit Risk Test") \
    .getOrCreate()

# Caminho do CSV no S3
s3_path = "s3a://credit-risk/raw/credit_risk_dataset.csv"

# Lê o arquivo
df = spark.read.csv(s3_path, header=True, inferSchema=True)

# Mostra as 5 primeiras linhas
df.show(5)

# Finaliza
spark.stop()
