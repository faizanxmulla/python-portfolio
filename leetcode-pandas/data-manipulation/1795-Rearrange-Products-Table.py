import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(products, id_vars='product_id', var_name='store', value_name='price').dropna()


# ===========================

# SOLUTION 2: without MELT function: 

# rearranged_rows = []
# for _, row in products.iterrows():
#     product_id = row['product_id']

#     for store_col in ['store1', 'store2', 'store3']:
#         price = row[store_col]
#         if pd.notna(price):
#             rearranged_rows.append((product_id, store_col, price))

# return pd.DataFrame(rearranged_rows, columns=['product_id', 'store', 'price'])

# ===========================

# SOLUTION 3: using STACK function

# products.set_index('product_id', inplace=True)
# products = products.stack(dropna=True).reset_index()

# products.columns = ['product_id','store','price']
# return pd.DataFrame(products)