import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    employees['total_time'] = employees.groupby(['emp_id', 'event_day'])['total_time'].transform('sum')
    
    employees.rename(columns={"event_day": "day"}, inplace=True)
    return employees[['day', 'emp_id', 'total_time']].drop_duplicates()


# NOTE: here only transform works because of the required output format.

# 1. .sum().reset_index() --> Reduces the number of rows by collapsing each group into a single row.
# 2. transform('sum') --> Does not reduce the number of rows. Instead, it repeats the aggregate value for each row in the group.
# 3. agg('sum') --> same as sum(), but just more flexible.



# SELECT   event_day AS day, 
#          emp_id,
#          SUM(out_time - in_time) AS total_time
# FROM     Employees
# GROUP BY 1, 2