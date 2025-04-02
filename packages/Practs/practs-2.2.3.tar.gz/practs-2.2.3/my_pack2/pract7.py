import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
def main():
    np.random.seed(42)
    n_users = 1000
    control_group = {
        'Group': 'Control',
        'User_ID': [f'C_{i}' for i in range(1, n_users + 1)],
        'Clicks': np.random.binomial(1, 0.05, n_users)}
    treatment_group = {
        'Group': 'Treatment',
        'User_ID': [f'T_{i}' for i in range(1, n_users + 1)],
        'Clicks': np.random.binomial(1, 0.06, n_users)}
    control_df = pd.DataFrame(control_group)
    treatment_df = pd.DataFrame(treatment_group)
    data = pd.concat([control_df, treatment_df], ignore_index=True)
    ctr_control = control_df['Clicks'].mean()
    ctr_treatment = treatment_df['Clicks'].mean()
    t_stat, p_value = ttest_ind(control_df['Clicks'], treatment_df['Clicks'])
    plt.bar(['Control', 'Treatment'], [ctr_control, ctr_treatment], color=['blue', 'orange'])
    plt.title('Click-Through Rate (CTR) Comparison')
    plt.ylabel('CTR')
    plt.ylim(0, 0.1)
    for i, ctr in enumerate([ctr_control, ctr_treatment]):
        plt.text(i, ctr + 0.002, f'{ctr:.2%}', ha='center', fontsize=12)
    plt.show()
    print("--- A/B Test Results ---")
    print(f"Control Group CTR: {ctr_control:.2%}")
    print(f"Treatment Group CTR: {ctr_treatment:.2%}")
    print(f"T-statistic: {t_stat:.4f}, P-value: {p_value:.4f}")
    if p_value < 0.05:
        print("The difference is statistically significant! The treatment group performed better.")
    else:
        print("No significant difference between the groups.")