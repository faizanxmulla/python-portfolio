import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    rich_count = store.query('amount > 500')['customer_id'].nunique()
    return pd.DataFrame({"rich_count": [rich_count]})



# SELECT COUNT(DISTINCT customer_id) as rich_count
# FROM   Store
# WHERE  amount > 500