import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [
            accounts.query('income < 20000').shape[0],
            accounts.query('income >= 20000 & income <= 50000').shape[0],
            accounts.query('income > 50000').shape[0]
        ],
    })
    


