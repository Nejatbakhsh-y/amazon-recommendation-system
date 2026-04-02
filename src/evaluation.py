# ============================================
# evaluation.py
# Model evaluation metrics
# ============================================

import numpy as np


def precision_at_k(actual, predicted, k=5):
    """
    Precision@K
    """
    predicted_top_k = predicted[:k]
    return len(set(predicted_top_k) & set(actual)) / k


def hit_rate(actual, predicted):
    """
    Hit Rate
    """
    return int(len(set(actual) & set(predicted)) > 0)
