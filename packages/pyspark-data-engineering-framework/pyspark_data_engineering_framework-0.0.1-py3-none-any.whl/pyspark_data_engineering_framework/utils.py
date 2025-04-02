from pyspark.sql.dataframe import DataFrame
from typing import List

def show_schema(df: DataFrame) -> None:
    """
    Print the schema of a DataFrame in a tree format.
    
    Args:
        df (DataFrame): PySpark DataFrame to display schema for
    """
    df.printSchema()

def count_rows(df: DataFrame) -> int:
    """
    Count the number of rows in a DataFrame.
    
    Args:
        df (DataFrame): PySpark DataFrame to count rows for
        
    Returns:
        int: Number of rows in the DataFrame
    """
    return df.count()

def get_columns(df: DataFrame) -> List[str]:
    """
    Get the list of column names in a DataFrame.
    
    Args:
        df (DataFrame): PySpark DataFrame to get columns from
        
    Returns:
        List[str]: List of column names
    """
    return df.columns