#simple content basses recomnder system

import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity

def main():
    data = {
        'movie_id': [1, 2, 3, 4, 5],
        'title': ["Inception", "The Matrix", "Interstellar", "Shutter Island", "The Prestige"],

        'genre': ['Sci-Fi', 'Sci-Fi', 'Sci-Fi', 'Thriller', 'Drama'],
        'description': ["A thief who steels coporate secrets through dream-sharing technology",
                        "A computer hacker learns about the true nature of his reality",
                        "Explores travel through a wormhole in space to ensure humanity's survival",
                        "A detective investigates the disappearance of a murderer from a asylum",
                        "Two magicians engage in a battle to create the ultimate stage illusion"]
    }

    df = pd.DataFrame(data)

    df['features'] = df['genre'] + " " + df['description']

    tfidf = TfidfVectorizer(stop_words='english')

    tfidf_matrix = tfidf.fit_transform(df['features'])

    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    def get_recommendations(title, cosine_sim=cosine_sim):
        idx = df[df['title'] == title].index[0]

        sim_scores = list(enumerate(cosine_sim[idx]))

        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        sim_indices = [i[0] for i in sim_scores[1:6]]

        return df['title'].iloc[sim_indices]

    recommendations = get_recommendations("Inception")

    print("Recommendations for Inception: ", recommendations.tolist())