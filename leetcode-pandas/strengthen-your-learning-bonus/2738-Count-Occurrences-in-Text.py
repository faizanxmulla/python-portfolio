import pandas as pd

data = {
    "content": [
        "The bull market is thriving.",
        "A bear market could be approaching.",
        "Investors are bullish on tech stocks.",
        "Some traders prefer a bear stance.",
        "The bull was spotted in the news.",
        "It was a mixed day, with both bull and bear sentiments.",
    ]
}

files = pd.DataFrame(data)


def word_count(files: pd.DataFrame) -> pd.DataFrame:
    bull_count = files["content"].str.contains(r"\bbull\b", case=False).sum()
    bear_count = files["content"].str.contains(r"\bbear\b", case=False).sum()

    return pd.DataFrame({"word": ["bull", "bear"], "count": [bull_count, bear_count]})

print(word_count(files))



# SELECT 'bull' AS word, COUNT(*) AS count
# FROM   files
# WHERE  content LIKE '% bull %'
# UNION
# SELECT 'bear' AS word, COUNT(*) AS count
# FROM   files
# WHERE  content LIKE '% bear %';
