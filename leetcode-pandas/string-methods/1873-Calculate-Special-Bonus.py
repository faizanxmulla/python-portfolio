import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = 0

    condition = employees.query('employee_id % 2 != 0 and not name.str.startswith("M")')
    employees.loc[condition.index, 'bonus'] = employees['salary']

    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')



# SELECT employee_id, 
#        CASE WHEN employee_id%2 <> 0 and name NOT LIKE 'M%' THEN salary ELSE 0 END as bonus
# FROM   employees 