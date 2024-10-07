import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return orders.groupby('customer_number')['order_number'].nunique().nlargest(1).reset_index()[['customer_number']]



# alternative solutions: 

#  1. using MODE() --> return orders['customer_number'].mode().to_frame()

#  2. orders = orders.groupby('customer_number', as_index=False).count()
#     orders.query('order_number == order_number.max()')[['customer_number']]



# SELECT   customer_number
# FROM     Orders
# GROUP BY 1
# ORDER BY count(customer_number) desc
# LIMIT    1