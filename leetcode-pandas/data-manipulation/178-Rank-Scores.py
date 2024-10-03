import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense', ascending= False)
    return scores.drop('id', axis=1).sort_values(by='score', ascending=False)



# corresponding SQL solution:

# SELECT score, DENSE_RANK() OVER(ORDER BY score desc) as rank
# FROM   scores