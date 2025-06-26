"""
Field selection and key-matching lookup for CSV dataset.
"""
import pandas as pd

def select_reference_field(df: pd.DataFrame, field: str):
    if field in df.columns:
        return df[field]
    else:
        raise ValueError(f"Field {field} not found in dataset.")

def lookup_by_key(df: pd.DataFrame, key_field: str, key_value):
    # Retrieve row(s) where key_field matches key_value
    return df[df[key_field] == key_value]
