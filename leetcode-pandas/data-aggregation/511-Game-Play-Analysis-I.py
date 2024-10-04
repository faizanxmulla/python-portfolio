import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity['first_login'] = activity.groupby('player_id')['event_date'].transform('min')
    return activity[['player_id', 'first_login']].drop_duplicates()


# alternative solution:
# return activity.groupby('player_id').agg(first_login=('event_date', 'min')).reset_index()


# NOTE:

# If you have a group with NaT and valid dates:

# 1) .min() will return NaT if any NaT values are present in the group.
# 2) .transform('min') will ignore NaT and return the earliest valid date.


# SELECT   player_id, min(event_date) as first_login
# FROM     activity
# GROUP BY 1