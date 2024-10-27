import pandas as pd

data = {
    "ad_id": [1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 4],
    "action": ["clicked", "viewed", "viewed", "clicked", "viewed", "clicked", "viewed", "viewed", "clicked", "viewed", "viewed", "viewed",],
}

ads = pd.DataFrame(data)

def calculate_ctr(ads: pd.DataFrame) -> pd.DataFrame:
    result = ads.groupby("ad_id").agg(
        clicks=("action", lambda x: (x == "clicked").sum()),
        total=("action", lambda x: ((x == "clicked") | (x == "viewed")).sum()),
    )

    result["ctr"] = (result["clicks"] / result["total"] * 100).fillna(0).round(2)
    result = result[["ctr"]].reset_index()

    return result.sort_values(["ctr", "ad_id"], ascending=[False, True])


print(calculate_ctr(ads))



# SELECT   ad_id,
#          ROUND(IFNULL(SUM(action = 'clicked') / SUM(action IN ('clicked', 'viewed')) * 100, 0), 2) AS ctr
# FROM     Ads
# GROUP BY 1
# ORDER BY 2 DESC, 1