#Building a hybrid recommender systemS

import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


def main():
    data = {
        "UserID": [1, 2, 3, 4, 5],
        "Item1": [5, 4, np.nan, 2, 1],
        "Item2": [4, np.nan, 4, 1, np.nan],
        "Item3": [1, 2, 3, np.nan, 5],
        "Item4": [np.nan, 3, 4, 5, 4]
    }
    df = pd.DataFrame(data).set_index("UserID")
    print("User-Item Interaction Matrix:\n", df)
    item_features = {
        "Item1": [1, 0, 0, 1],
        "Item2": [0, 1, 0, 1],
        "Item3": [0, 0, 1, 1],
        "Item4": [1, 1, 0, 0]
    }

    item_features_df = pd.DataFrame(item_features).T
    similarity_matrix = cosine_similarity(item_features_df)
    print("\n Item Similarity Matrix:\n", similarity_matrix)

    def content_based_recommendation(user_ratings, similarity_matrix):
        user_ratings = np.nan_to_num(user_ratings)
        scores = np.dot(user_ratings, similarity_matrix)
        return scores / np.sum(similarity_matrix, axis=1)

    content_predictions = np.apply_along_axis(
        content_based_recommendation, axis=1, arr=df.fillna(0).values, similarity_matrix=similarity_matrix)
    print("\n Content based Predictions:\n", content_predictions)
    user_similarity = cosine_similarity(df.fillna(0))
    print("\n User Similarity Matrix:\n", user_similarity)
    collaborative_predictions = np.dot(user_similarity, df.fillna(0)) / np.sum(user_similarity, axis=1)[
                                                                        :, None]
    print("\n Collaborative Filtering Predictions:\n", collaborative_predictions)
    weights = [0.6, 0.4]
    hybrid_predictions = weights[0] * collaborative_predictions + weights[1] * content_predictions
    print("\n Hybrid Recommendations:\n", hybrid_predictions)
    ground_truth = {
        "UserID": [1, 2, 3, 4, 5],
        "Item1": [5, 4, 3, 2, 1],
        "Item2": [4, 3, 4, 1, 2],
        "Item3": [1, 2, 3, 4, 5],
        "Item4": [2, 3, 4, 5, 4]}
    ground_truth_df = pd.DataFrame(ground_truth).set_index("UserID").values
    rmse = np.sqrt(mean_squared_error(ground_truth_df.flatten(), hybrid_predictions.flatten()))
    print(f"\n RMSE of Hybrid Model: {rmse:.4f}")

main()