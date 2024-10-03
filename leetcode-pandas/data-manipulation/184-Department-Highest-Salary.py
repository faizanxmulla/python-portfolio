import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    return employee.merge(
        department.rename(columns={'name': 'Department'}), 
        left_on='departmentId', 
        right_on='id'
    ).rename(columns={'name': 'Employee'}
    ).groupby(
        'departmentId'
    ).apply(
        lambda x: x[x['salary'] == x['salary'].max()]
    ).reset_index(drop=True)[
        ['Department', 'Employee', 'salary']
    ].rename(columns={
        'salary': 'Salary'
    })


# Solution 2: using idxmax()



# corresponding SQL solution:

# WITH ranked_salaries as (
#     SELECT d.name as Department, 
#            e.name as Employee, 
#            e.salary as Salary,
#            RANK() OVER(partition by departmentId order by salary desc)
#     FROM   Employee e JOIN Department d ON e.departmentId=d.id 
# )
# SELECT Department, Employee, Salary
# FROM   ranked_salaries 
# WHERE  rank=1