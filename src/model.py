# ============================================
# model.py
# Recommendation model using SVD
# ============================================

import numpy as np
from scipy.sparse.linalg import svds


def train_svd(interaction_matrix, k=20):
    """
    Train SVD model
    """
    U, sigma, Vt = svds(interaction_matrix, k=k)
    sigma = np.diag(sigma)
    predicted_ratings = np.dot(np.dot(U, sigma), Vt)
    return predicted_ratings


def recommend_products(predicted_ratings, user_index, top_n=5):
    """
    Recommend top N products for a user
    """
    user_ratings = predicted_ratings[user_index]
    top_items = np.argsort(user_ratings)[::-1][:top_n]
    return top_items
