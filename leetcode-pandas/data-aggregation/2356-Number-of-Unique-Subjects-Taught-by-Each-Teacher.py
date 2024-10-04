import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    teacher['cnt'] = teacher.groupby(by="teacher_id")['subject_id'].transform('nunique')
    return teacher[['teacher_id', 'cnt']].drop_duplicates()



# SELECT   teacher_id, COUNT(DISTINCT subject_id) as cnt
# FROM     teacher
# GROUP BY 1