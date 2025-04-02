import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")
tags = pd.read_csv("tags.csv")

print("Movies Data: ")
print(movies.head())

print("Ratings Data: ")
print(ratings.head())

def recommend_popular_movies(ratings, movies, top_n=5):
    movie_ratings = ratings.groupby("movieId")["rating"].mean().reset_index()  # Correct column name
    movie_ratings = movie_ratings.sort_values("rating", ascending=False).head(top_n)
    popular_movies = pd.merge(movie_ratings, movies, on="movieId")  # Merge on the correct column
    return popular_movies[["title", "rating"]]

print("\n Popular Movie Recommendations: ")
print(recommend_popular_movies(ratings, movies))

def content_based_recommendations(movie_title, movies, top_n=5):
    movies["content"] = movies["genres"]
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(movies["content"])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    idx = movies[movies["title"] == movie_title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1]

    movie_indices = [i[0] for i in sim_scores]
    return movies["title"].iloc[movie_indices]

movie_title = "Toy Story (1995)"
print(f"\n Content-Based Recommendations for '{movie_title}':")
print(content_based_recommendations(movie_title, movies))
