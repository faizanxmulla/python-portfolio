import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    counts = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='count')
    return counts.query('count >= 3')[['actor_id', 'director_id']]



# SELECT   actor_id, director_id
# FROM     ActorDirector
# GROUP BY 1, 2
# HAVING   COUNT(*) >= 3