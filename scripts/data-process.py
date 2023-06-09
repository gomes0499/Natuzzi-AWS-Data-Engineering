from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DecimalType, DateType

def main():
    spark = SparkSession.builder \
        .appName("CSV to Parquet Converter") \
        .getOrCreate()

    table_names = ["category", "city", "customer", "product", "Order", "orderitem"]
    parquet_path = "s3://wu1process/parquet/"

    schemas = {
        "category": StructType([
            StructField("CategoryID", IntegerType(), True),
            StructField("CategoryName", StringType(), True)
        ]),
        "city": StructType([
            StructField("CityID", IntegerType(), True),
            StructField("CityName", StringType(), True),
            StructField("State", StringType(), True)
        ]),
        "customer": StructType([
            StructField("CustomerID", IntegerType(), True),
            StructField("CityID", IntegerType(), True),
            StructField("FirstName", StringType(), True),
            StructField("LastName", StringType(), True),
            StructField("Email", StringType(), True),
            StructField("Phone", StringType(), True)
        ]),
        "product": StructType([
            StructField("ProductID", IntegerType(), True),
            StructField("CategoryID", IntegerType(), True),
            StructField("ProductName", StringType(), True),
            StructField("ProductDescription", StringType(), True),
            StructField("ProductPrice", DecimalType(10, 2), True),
            StructField("ProductInventory", IntegerType(), True)
        ]),
        "Order": StructType([
            StructField("OrderID", IntegerType(), True),
            StructField("CustomerID", IntegerType(), True),
            StructField("OrderDate", DateType(), True),
            StructField("TotalAmount", DecimalType(10, 2), True)
        ]),
        "orderitem": StructType([
            StructField("OrderItemID", IntegerType(), True),
            StructField("OrderID", IntegerType(), True),
            StructField("ProductID", IntegerType(), True),
            StructField("Quantity", IntegerType(), True),
            StructField("Price", DecimalType(10, 2), True)
        ])
    }

    for table_name in table_names:
        csv_path = f"s3://wu1landing/raw_data/public/{table_name}/*.csv"
        schema = schemas[table_name]

        df = (spark.read
              .format("csv")
              .schema(schema)
              .option("header", True)
              .option("delimiter", ",")
              .load(csv_path))

        df.write \
            .format("parquet") \
            .mode("overwrite") \
            .save(f"{parquet_path}{table_name}")

if __name__ == "__main__":
    main()
