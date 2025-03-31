import pandas as pd

def console_input():
    """
    Reads input from the console.
    """
    return input("Enter text: ")

def file_input(file_path):
    """
    Reads input from file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def pandas_input(file_path):
    """
    Reads input from a pandas DataFrame.
    """
    return pd.read_csv(file_path, header=None).to_string(index=False)