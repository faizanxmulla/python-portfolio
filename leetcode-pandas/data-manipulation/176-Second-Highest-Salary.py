import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted_salaries = employee[['salary']].drop_duplicates().sort_values(by='salary', ascending=False)

    if len(sorted_salaries) >= 2:
        second_highest = sorted_salaries.iloc[1:2]
    else:
        second_highest = pd.DataFrame({'salary': [None]})
    
    second_highest.columns = ['SecondHighestSalary']
    return second_highest