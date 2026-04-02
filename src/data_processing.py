# ============================================
# data_processing.py
# Load and preprocess data
# ============================================

import pandas as pd


def load_data(path):
    """Load dataset from CSV"""
    return pd.read_csv(path)


def clean_data(df):
    """Basic cleaning"""
    df = df.dropna()
    return df


def create_interaction_matrix(df):
    """
    Create user-item interaction matrix
    """
    interaction_matrix = df.pivot_table(
        index="user_id",
        columns="product_id",
        values="interaction_score",
        fill_value=0
    )
    return interaction_matrix
