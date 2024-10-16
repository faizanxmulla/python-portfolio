import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders_red = orders.merge(company[company['name'] == 'RED'], on='com_id', how='inner')
    sales_to_red = orders_red['sales_id'].unique()
    
    return sales_person[~sales_person['sales_id'].isin(sales_to_red)][['name']]
    


# SELECT sp.name
# FROM   orders o JOIN company c ON (o.com_id = c.com_id AND c.name = 'RED')
#                 RIGHT JOIN SalesPerson sp ON sp.sales_id = o.sales_id
# WHERE  o.sales_id IS NULL 