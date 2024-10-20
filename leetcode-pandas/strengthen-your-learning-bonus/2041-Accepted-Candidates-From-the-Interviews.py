import pandas as pd

candidates_data = {
    "candidate_id": [11, 9, 6, 8],
    "name": ["Atticus", "Ruben", "Aliza", "Alfredo"],
    "years_of_exp": [1, 6, 10, 0],
    "interview_id": [101, 104, 109, 107],
}

rounds_data = {
    "interview_id": [109, 101, 109, 107, 104, 109, 104, 104, 109, 104, 107, 101],
    "round_id": [3, 2, 4, 1, 3, 1, 4, 1, 2, 2, 2, 1],
    "score": [4, 8, 1, 3, 6, 4, 7, 2, 1, 7, 3, 8],
}

candidates = pd.DataFrame(candidates_data)
rounds = pd.DataFrame(rounds_data)


def get_candidates(candidates: pd.DataFrame, rounds: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(candidates, rounds, how='left', on='interview_id')
    merged_df = merged_df.query('years_of_exp >= 2')

    merged_df['sum'] = merged_df.groupby('candidate_id')['score'].transform('sum')
    return merged_df.query('sum > 15')[['candidate_id']].drop_duplicates()


print(get_candidates(candidates, rounds))



# SELECT   candidate_id
# FROM     candidates c LEFT JOIN rounds r USING(interview_id)
# WHERE    years_of_exp >= 2
# GROUP BY 1
# HAVING   SUM(score) > 15;