import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    cross_join = students.merge(subjects, how='cross')
    exam_counts = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')

    result = cross_join.merge(exam_counts, on=['student_id', 'subject_name'], how='left')

    result['attended_exams'] = result['attended_exams'].fillna(0).astype(int)
    result = result.sort_values(['student_id', 'subject_name'])

    return result[['student_id', 'student_name', 'subject_name', 'attended_exams']].reset_index(drop=True)



# SELECT   s.student_id, s.student_name, su.subject_name, COUNT(e.student_id) as attended_exams
# FROM     Students s JOIN Subjects su LEFT JOIN Examinations e ON s.student_id = e.student_id
#                                                          AND su.subject_name = e.subject_name
# GROUP BY 1, 2, 3
# ORDER BY 1, 3