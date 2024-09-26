import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left')
    merged_df = merged_df[merged_df['customerId'].isnull()]

    return merged_df[['name']].rename(columns={'name': 'Customers'})


# ALTERNATIVE solution: using unique() and isin()

# order_ids = orders['customerId'].unique()
# result = customers[~customers['id'].isin(order_ids)]

# return result[['name']].rename(columns={'name': 'Customers'})


    