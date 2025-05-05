"""
Module 2: Initial Script to Verify Project Setup
File: scripts/data_prep.py
"""

#####################################
# Import Modules at the Top
#####################################

# Import from Python Standard Library
import pathlib
import sys

# Import from external packages
import pandas as pd

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))

# Import local modules (e.g. utils/logger.py)
from utils.logger import logger

# Constants
SCRIPTS_DIR: pathlib.Path = pathlib.Path(__file__).resolve().parent  # Directory of the current script
PROJECT_ROOT: pathlib.Path = SCRIPTS_DIR.parent  # Navigate to the project's root directory
DATA_DIR: pathlib.Path = PROJECT_ROOT/ "data" # Directory for ALL data files
RAW_DATA_DIR: pathlib.Path = DATA_DIR / "raw"  # Directory for raw data files

# Ensure the data directories exist or create them
DATA_DIR.mkdir(exist_ok=True)
RAW_DATA_DIR.mkdir(exist_ok=True)


def read_raw_data(file_name: str) -> pd.DataFrame:
    """Read raw data from CSV."""
    file_path: pathlib.Path = RAW_DATA_DIR.joinpath(file_name)
    try:
        logger.info(f"READING: {file_path}.")
        return pd.read_csv(file_path)
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return pd.DataFrame()  # Return an empty DataFrame if the file is not found
    except Exception as e:
        logger.error(f"Error reading {file_path}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame if any other error occurs

def process_data(file_name: str) -> None:
    """Process raw data by reading it into a pandas DataFrame object."""
    df = read_raw_data(file_name)
    if df.empty:
        logger.warning(f"No data to process for {file_name}.")
        return
    logger.info(f"Processing data for {file_name}.")
    logger.info(f"Data shape (ct of rows, ct of columns): {df.shape}.")
    logger.info(f"Data columns: {df.columns.tolist()}.")

def main() -> None:
    """Main function for processing raw customer, product, and sales data."""
    logger.info("Starting data preparation...")

    # Each pathlib.Path object has a method iterdir() that returns an iterator over the files in the directory
    # Call this method and if there are not any entries, log an error message
    # and return from the function to avoid further processing
    if not any(RAW_DATA_DIR.iterdir()):
        logger.error("The data/raw folder is empty. Please add raw data files to the data/raw directory.")
        return
    
    # Process each data file one at a time
    # Note: The file names must match the actual files in your RAW_DATA_DIR
    process_data("customers_data.csv")
    process_data("products_data.csv")
    process_data("sales_data.csv")

    logger.info("Data preparation complete.")


# Conditional execution block that calls main() only when this file is executed directly
# This is a common Python idiom to allow or prevent parts of code from being run when the modules are imported
if __name__ == "__main__":
    main()
