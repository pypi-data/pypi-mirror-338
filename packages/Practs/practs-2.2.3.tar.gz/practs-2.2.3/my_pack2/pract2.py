# Applying matrix factorization for recommendation.



import numpy as np
from sklearn.metrics import mean_squared_error

def main():
    R = np.array([
        [5, 3, 0, 1],
        [4, 0, 0, 1],
        [1, 1, 0, 5],
        [0, 0, 5, 4],
        [0, 3, 4, 0]
    ])
    num_users, num_items = R.shape
    num_factors = 2
    alpha = 0.01
    lambda_reg = 0.1
    num_epochs = 5000
    P = np.random.rand(num_users, num_factors)
    Q = np.random.rand(num_items, num_factors)

    def calculate_rmse(R, P, Q):
        predicted_R = np.dot(P, Q.T)
        mask = R > 0
        mse = mean_squared_error(R[mask], predicted_R[mask])
        return np.sqrt(mse)

    for epoch in range(num_epochs):
        for i in range(num_users):
            for j in range(num_items):
                if R[i, j] > 0:
                    error = R[i, j] - np.dot(P[i, :], Q[j, :].T)
                    P[i, :] += alpha * (2 * error * Q[j, :] - lambda_reg * P[i, :])
                    Q[j, :] += alpha * (2 * error * P[i, :] - lambda_reg * Q[j, :])
            if (epoch + 1) % 1000 == 0:
                rmse = calculate_rmse(R, P, Q)
                print(f"Epoch{epoch + 1}/{num_epochs},RMSE:{rmse:.4f}")
    predicted_R = np.dot(P, Q.T)
    print("\nOriginal Ratings Mayrix (R):")
    print(R)
    print("\nPredicted Ratings Matrix:")
    print(np.round(predicted_R, 2))