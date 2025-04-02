import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix
ratings = pd.read_csv("ratings.csv")
movies = pd.read_csv("movies.csv")
user_item_matrix = ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)
user_item_sparse = csr_matrix(user_item_matrix)
user_similarity = cosine_similarity(user_item_sparse)
np.fill_diagonal(user_similarity, 0)
def add_laplace_noise(matrix, scale=0.5):
    noise = np.random.laplace(loc=0, scale=scale, size=matrix.shape)
    return matrix + noise
private_similarity = add_laplace_noise(user_similarity, scale=0.5)
def recommend_movies(user_id, similarity_matrix, user_item_matrix, top_n=5):
    similar_users = np.argsort(-similarity_matrix[user_id])[:10]
    avg_ratings = user_item_matrix.iloc[similar_users].mean(axis=0)
    unseen_movies = user_item_matrix.iloc[user_id] == 0
    recommendations = avg_ratings[unseen_movies].sort_values(ascending=False).head(top_n)
    return recommendations. index.tolist()
user_id = 10
original_recommendations = recommend_movies(user_id, user_similarity, user_item_matrix)
private_recommendations=recommend_movies(user_id , private_similarity, user_item_matrix)
print("OriginalRecommendations:",movies[movies['movieId'].isin(original_recommendations)])
print("\nPrivacy-PreservedRecommendations:",movies[movies['movieId'].isin(private_recommendations)])