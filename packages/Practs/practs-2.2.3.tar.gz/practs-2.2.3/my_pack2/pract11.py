#: Visualization of recommendation results and user preferences.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from surprise import Dataset,SVD
from surprise.model_selection import train_test_split
from surprise import Reader, Dataset, SVD
def main():
    ratings_df = pd.read_csv('ratings.csv')
    movies_df = pd.read_csv('movies.csv')
    ratings_df = ratings_df.merge(movies_df, on='movieId')
    ratings_df.head()
    plt.figure(figsize=(8, 4))
    sns.histplot(ratings_df['rating'], bins=10, kde=True, color='blue')
    plt.title("Distribution of Movie Ratings")
    plt.xlabel("Rating")
    plt.ylabel("Count")
    plt.show()
    top_movies = ratings_df.groupby("title")["rating"].mean().sort_values(ascending=False).head(
        10)
    plt.figure(figsize=(10, 5))
    sns.barplot(x=top_movies.values, y=top_movies.index, palette="viridis")
    plt.title("Top 10 Movies by Average Rating")
    plt.xlabel("Average Rating")
    plt.show()
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(ratings_df[['userId', 'movieId', 'rating']], reader)
    trainset, testset = train_test_split(data, test_size=0.2)
    svd = SVD()
    svd.fit(trainset)

    def recommened_movies(userId, model, ratings_df, num_recs=5):
        unique_movies = ratings_df['movieId'].unique()
        predictions = [model.predict(userId, movie_id) for movie_id in unique_movies]
        predictions.sort(key=lambda x: x.est, reverse=True
        return [(p.iid, p.est) for p in predictions[:num_recs]]

    recommenedations = recommened_movies(1, svd, ratings_df)
    rec_df = pd.DataFrame(recommenedations, columns=['movieId', 'predicted_rating'])
    rec_df = rec_df.merge(movies_df, on='movieId')
    print(rec_df)