import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()
    # users['name'] = users['name'].str[0].str.upper() + users['name'].str[1:].str.lower()

    return users.sort_values(by='user_id')



# SELECT user_id, CONCAT(UPPER(SUBSTRING(name, 1, 1)), LOWER(SUBSTRING(name, 2))) as name
# FROM   users