from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType
from pyspark.sql.functions import from_json, to_json, struct, date_format
from google.cloud import storage
from datetime import datetime
from pyspark.sql import SparkSession

bucket_name = "bitirme1"
project_id = "eloquent-petal-379005"

# Google Cloud Storage bağlantısını yapılandırma
client = storage.Client(project=project_id)
bucket = client.bucket(bucket_name)

spark = SparkSession.builder \
    .appName("Spark") \
    .getOrCreate()

kafkaDF = spark.readStream.format("kafka").option("kafka.bootstrap.servers","34.125.86.34:9092").option("subscribe","ornek").load()

schema = StructType([
    StructField("vehicle_id", StringType(), True),
    StructField("date", StringType(), True),
    StructField("hour", IntegerType(), True),
    StructField("minute", IntegerType(), True),
    StructField("latitude", FloatType(), True),
    StructField("longitude", FloatType(), True),
    StructField("tire_pressure", FloatType(), True),
    StructField("speed", FloatType(), True),
    StructField("temperature", FloatType(), True),
    StructField("gas_composition", StringType(), True)
])

activationDF = kafkaDF.select(from_json(kafkaDF["value"].cast("string"), schema).alias("activation")) 

df = activationDF.select("activation.interval","activation.date_time_", "activation.ip", "activation.url", "activation.status",
                "activation.size", "activation.duration"
                )


# Cloud Storage yolunu oluşturma
date_str = datetime.now().strftime("%Y-%m-%d")
path = f"gs://{bucket_name}/{date_str}/"

# JSON dosyalarını Cloud Storage'a kaydetme
json_writer_query = df.writeStream \
    .format("json") \
    .option("checkpointLocation", f"{path}/checkpoint") \
    .option("path", path) \
    .option("ignoreChanges", "true") \
    .option("ignoreDeletes", "true") \
    .option("ignoreFileNotFound", "true") \
    .start()

# İşlemi durdurmak için:
# json_writer_query.stop()
