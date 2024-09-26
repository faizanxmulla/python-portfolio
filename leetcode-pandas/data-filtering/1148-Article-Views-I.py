import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    result_df = (
        views
            .query('author_id == viewer_id')
            .groupby('author_id')
            .size()
            .reset_index(name='count')
            .sort_values(by='author_id')
            .rename(columns={'author_id': 'id'})
            .reset_index(drop=True)
        )
    
    return result_df[['id']]


# corresponding SQL solution: 

# SELECT   author_id as id 
# FROM     views
# WHERE    author_id=viewer_id
# GROUP BY 1
# HAVING   COUNT(view_date) >= 1