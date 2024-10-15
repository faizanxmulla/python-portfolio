import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    merged_df = employee.merge(employee, how='inner', left_on='managerId', right_on='id', suffixes=('', '_manager'))
    grouped_df = merged_df.groupby(['managerId', 'name_manager'], dropna=False)['id'].size().reset_index(name='count')
    
    result = grouped_df.query('count >= 5')[['name_manager']]
    return result.rename(columns={'name_manager': 'name'}).reset_index(drop=True)


# SELECT m.name 
# FROM Employee e, Employee m 
# WHERE m.id = e.managerId
# GROUP BY e.managerId
# HAVING COUNT(e.id) >= 5