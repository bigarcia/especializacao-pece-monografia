from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer, VectorAssembler, StandardScaler
from pyspark.sql.types import DoubleType
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("CreditRisk_Enrich") \
    .config("spark.jars", "/home/ec2-user/jars/hadoop-aws-3.3.4.jar,/home/ec2-user/jars/aws-java-sdk-bundle-1.12.375.jar") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.aws.credentials.provider", "com.amazonaws.auth.DefaultAWSCredentialsProviderChain") \
    .getOrCreate()

# Leitura da camada clean
df_clean = spark.read.parquet("s3a://credit-risk/clean/")

# Indexação de variáveis categóricas
indexer = StringIndexer(
    inputCols=[
        "person_home_ownership", "loan_intent",
        "loan_grade", "cb_person_default_on_file"
    ],
    outputCols=[
        "person_home_ownership_indexed", "loan_intent_indexed",
        "loan_grade_indexed", "cb_person_default_on_file_indexed"
    ]
)

df_indexed = indexer.fit(df_clean).transform(df_clean)

# Colunas para vetorização
feature_cols = [
    "person_age", "person_income", "person_emp_length", "loan_amnt",
    "loan_int_rate", "loan_percent_income", "cb_person_cred_hist_length",
    "person_home_ownership_indexed", "loan_intent_indexed",
    "loan_grade_indexed", "cb_person_default_on_file_indexed"
]

# Garantir tipos Double
for c in feature_cols:
    df_indexed = df_indexed.withColumn(c, col(c).cast(DoubleType()))

# Remove registros com null nas colunas usadas no modelo
df_indexed = df_indexed.dropna(subset=feature_cols)

# Criação do vetor de features
assembler = VectorAssembler(inputCols=feature_cols, outputCol="numeric_features_assembled")
df_assembled = assembler.transform(df_indexed)

# Escalonamento dos dados
scaler = StandardScaler(inputCol="numeric_features_assembled", outputCol="numeric_features_scaled")
df_scaled = scaler.fit(df_assembled).transform(df_assembled)

# Escrita na camada enrich
df_scaled.write.mode("overwrite").parquet("s3a://credit-risk/enrich/")

print("✅ Dados enriquecidos salvos na camada enrich.")
spark.stop()
