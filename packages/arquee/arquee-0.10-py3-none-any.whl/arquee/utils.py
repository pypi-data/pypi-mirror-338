from os.path import exists, join
from .config import datalake, datamart
from .tools.db import get_db_url
from pyspark.sql import DataFrame
from pyspark.sql import SparkSession
from dotenv import load_dotenv
from pyspark.sql.functions import initcap, trim
from os import listdir

load_dotenv()


def create_datalake(file_name: str = "arquee.txt", clean: bool = True):
    origin = get_db_url("ORIGIN_DB")

    if not exists(datalake):
        raise FileNotFoundError("Folder datalake not found, run command Arquee")

    if exists(file_name):
        spark = get_spark_session()
        with open(file_name, "r") as file:
            tables = set(table.upper().strip() for table in file.readlines())

    for table in tables:
        destiny_path = join(datalake, table)
        df: DataFrame = spark.read.jdbc(origin, table)

        if clean:
            for column in df.columns:
                df = df.withColumn(column, trim(initcap(column)))

            df = df.fillna("No encontrado")
            df = df.replace("", value="No encontrado")

        df.write.parquet(destiny_path, mode="overwrite")


spark = None


def get_spark_session() -> SparkSession:
    global spark
    if not spark:
        spark = (
            SparkSession.builder.appName("ETL")
            .master("local[*]")
            .config("spark.executor.memory", "4g")
            .config("spark.sql.parquet.int96RebaseModeInWrite", "CORRECTED")
            .getOrCreate()
        )
        spark.sparkContext.setLogLevel("ERROR")
    return spark


def get_dataframe(table_name: str, standart_location: bool = True):
    spark: SparkSession = get_spark_session()

    if standart_location:
        folder_path = join(datalake, table_name.upper().strip())
    else:
        folder_path = join(datamart, table_name.upper().strip())

    if not exists(folder_path):
        raise FileNotFoundError("Folder not found, check datalake folder")
    df: DataFrame = spark.read.parquet(folder_path)
    return df


def save_dataframe(df: DataFrame, table_name: str):
    folder_path = join(datamart, table_name.upper().strip())
    df.write.parquet(folder_path, "overwrite")


def save_datamart():
    destiny = get_db_url("DESTINY_DB")
    dm_tables = listdir(datamart)
    print(dm_tables)
    for table in dm_tables:
        df = get_dataframe(table, standart_location=False)
        df.write.jdbc(destiny, table, mode="overwrite")


if __name__ == "__main__":
    # create_datalake(clean=False)
    save_datamart()
