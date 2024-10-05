import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses['count'] = courses.groupby('class')['student'].transform('nunique')
    return courses.query('count >= 5')[['class']].drop_duplicates()



# SELECT   class
# FROM     courses
# GROUP BY 1
# HAVING   COUNT(student) >= 5