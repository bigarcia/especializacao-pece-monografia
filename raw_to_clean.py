from pyspark.sql.functions import col, when, count, trim
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Data Cleaning") \
    .config("spark.jars", "/home/ec2-user/jars/hadoop-aws-3.3.4.jar,/home/ec2-user/jars/aws-java-sdk-bundle-1.12.375.jar") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.aws.credentials.provider", "com.amazonaws.auth.DefaultAWSCredentialsProviderChain") \
    .getOrCreate()

s3_input_path = "s3a://credit-risk/raw/credit_risk_dataset.csv"
df = spark.read.csv(s3_input_path, header=True, inferSchema=True)

df.printSchema()



categorical_cols = [c for c, t in df.dtypes if t == "string"]
numeric_cols = [c for c, t in df.dtypes if t in ["double", "int"]]



print(f"Número de linhas antes: {df.count()}")
df = df.dropDuplicates()
print(f"Número de linhas depois: {df.count()}")


df = df.fillna({c: "Unknown" for c in categorical_cols})

df = df.filter((col("person_age") >= 18) & (col("person_age") <= 100))

df = df.filter(col("person_income") > 0)


df = df.filter((col("loan_int_rate") > 0) & (col("loan_int_rate") < 100))


df = df.withColumn(
    "loan_percent_income",
    when(
        col("loan_percent_income") == 0,
        (col("loan_amnt") / col("person_income")).cast("double")
    ).otherwise(col("loan_percent_income"))
)


df = df.filter(
    (col("cb_person_cred_hist_length").isNotNull()) &
    (col("cb_person_cred_hist_length") >= 1)
)


df = df.filter((col("loan_status") == 0) | (col("loan_status") == 1))


df = df.filter(col("person_income") <= 300000)

# Salva como Parquet na camada trusted
s3_output_path = "s3a://credit-risk/clean/"

df.write.mode("overwrite").parquet(s3_output_path)

print("Arquivo salvo na camada clean")
