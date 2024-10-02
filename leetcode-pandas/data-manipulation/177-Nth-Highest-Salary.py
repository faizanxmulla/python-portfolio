import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sorted_salaries = employee[['salary']].drop_duplicates().sort_values(by='salary', ascending=False)

    if 0 < N <= len(sorted_salaries) :
        nth_highest = sorted_salaries.iloc[N-1:N]
    else: 
        nth_highest = pd.DataFrame({'salary': [None]})
    
    nth_highest.columns = [f'getNthHighestSalary({N})']
    return nth_highest