import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    return daily_sales.groupby(['date_id', 'make_name']).agg(
        unique_leads=('lead_id', 'nunique'),
        unique_partners=('partner_id', 'nunique')
    ).reset_index()




# SELECT   date_id, 
#          make_name, 
#          COUNT(DISTINCT lead_id) AS unique_leads, 
#          COUNT(DISTINCT partner_id) AS unique_partners
# FROM     DailySales
# GROUP BY 1, 2
# ORDER BY 1, 2