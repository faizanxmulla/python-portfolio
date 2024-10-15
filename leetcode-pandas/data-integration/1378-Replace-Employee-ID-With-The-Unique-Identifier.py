import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    return employees.merge(employee_uni, how='left', on='id')[['unique_id', 'name']]



# SELECT unique_id, name
# FROM Employees e LEFT JOIN EmployeeUNI eu ON e.id = eu.id