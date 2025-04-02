from pyspark.sql import SparkSession
from pyspark.sql.dataframe import DataFrame
from pyspark_data_engineering_framework.exceptions import UnsupportedFileFormatException

def read_csv(spark: SparkSession, file_path: str, **options) -> DataFrame:
    """
    Read a CSV file into a PySpark DataFrame.
    
    Args:
        spark (SparkSession): Active SparkSession
        file_path (str): Path to the CSV file
        **options: Additional options to pass to spark.read.csv()
        
    Returns:
        DataFrame: PySpark DataFrame containing the CSV data
    """
    return spark.read.csv(file_path, **options)

def read_json(spark: SparkSession, file_path: str, **options) -> DataFrame:
    """
    Read a JSON file into a PySpark DataFrame.
    
    Args:
        spark (SparkSession): Active SparkSession
        file_path (str): Path to the JSON file
        **options: Additional options to pass to spark.read.json()
        
    Returns:
        DataFrame: PySpark DataFrame containing the JSON data
    """
    return spark.read.json(file_path, **options)

def read_xml(spark: SparkSession, file_path: str, **options) -> DataFrame:
    """
    Read an XML file into a PySpark DataFrame.
    Requires the com.databricks:spark-xml package to be available.
    
    Args:
        spark (SparkSession): Active SparkSession
        file_path (str): Path to the XML file
        **options: Additional options to pass to spark.read.format('xml')
        
    Returns:
        DataFrame: PySpark DataFrame containing the XML data
        
    Raises:
        UnsupportedFileFormatException: If spark-xml package is not available
    """
    try:
        return spark.read.format('xml').load(file_path, **options)
    except Exception as e:
        if "Failed to find data source: xml" in str(e):
            raise UnsupportedFileFormatException(
                "XML support requires com.databricks:spark-xml package. "
                "Please ensure the package is available in your Spark environment."
            ) from e
        raise