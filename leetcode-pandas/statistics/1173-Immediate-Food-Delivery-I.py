import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    immediate_deliveries = delivery.query('order_date == customer_pref_delivery_date').shape[0]
    total_deliveries = len(delivery)

    immediate_percentage = 100.0 * (immediate_deliveries / total_deliveries)
    return pd.DataFrame({"immediate_percentage": [round(immediate_percentage, 2)]})



# SELECT ROUND(100.0 * COUNT(delivery_id) FILTER(WHERE order_date=customer_pref_delivery_date) / COUNT(delivery_id), 2) as immediate_percentage
# FROM   Deliveries