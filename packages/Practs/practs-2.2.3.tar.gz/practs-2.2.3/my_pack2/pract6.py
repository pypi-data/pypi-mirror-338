import pandas as pd

from sklearn.metrics import precision_score, recall_score, f1_score

ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')

threshold = 4.0
user_actual_relevent = (ratings[ratings['rating'] >= threshold].groupby('userId')['movieId'].apply(set))

top_movies = set(ratings['movieId'].value_counts().head(10).index)
user_recommended = {user: top_movies for user in user_actual_relevent.index}

evaluation_data = pd.DataFrame({'user_id': user_actual_relevent.index,
                                'actual_relevant': user_actual_relevent.values,
                                'recommended': user_actual_relevent.index.map(user_recommended.get)})

precision_list = []
recall_list = []
f1_list = []

for index, row in evaluation_data.iterrows():
    actual = row['actual_relevant']
    recommended = row['recommended']

    if not isinstance(actual, set):
        actual = set(actual)

    if not isinstance(recommended, set):
        recommended = set(recommended)

    all_items = actual.union(recommended)
    actual_vector = [1 if item in actual else 0 for item in all_items]
    recommended_vector = [1 if item in recommended else 0 for item in all_items]

    try:
        precision = precision_score(actual_vector, recommended_vector, zero_division=0)
        recall = recall_score(actual_vector, recommended_vector, zero_division=0)
        f1 = f1_score(actual_vector, recommended_vector, zero_division=0)
    except ValueError:
        precision, recall, f1 = 0.0, 0.0, 0.0

    precision_list.append(precision)
    recall_list.append(recall)
    f1_list.append(f1)

    evaluation_data['precision'] = precision_list
    evaluation_data['recall'] = recall_list
    evaluation_data['f1_score'] = f1_list
    avg_precision = sum(precision_list) / len(precision_list)
    avg_recall = sum(recall_list) / len(recall_list)
    avg_f1_score = sum(f1_list) / len(f1_list)
    print("Evaluation Results for each user:")
    print(evaluation_data[['user_id', 'precision', 'recall', 'f1_score']])
    print("\nOverall Metrics:")
    print(f"Average Precision:{avg_precision:.2f}")
    print(f"Average Recall:{avg_recall:.2f}")
    print(f"Average F1-score:{avg_f1_score:.2f}")
