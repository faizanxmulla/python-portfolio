import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    return activities.groupby('sell_date').agg(
        num_sold=('product', 'nunique'),
        products=('product', lambda x: ','.join(sorted(x.unique())))
    ).reset_index()
    


# my initial approach: 

# activities['num_sold'] = activities.groupby('sell_date')['product'].transform('nunique')
# activities['products'] = activities.groupby('sell_date').str.cat(activities['products'], sep=',')
    
# return activities[['sell_date', 'num_sold', 'products']].drop_duplicates()




# SELECT   sell_date, 
#          COUNT(DISTINCT product ) as num_sold, 
#          STRING_AGG(DISTINCT product, ',' ORDER BY product) as products
# FROM     Activities 
# GROUP BY 1
# ORDER BY 1