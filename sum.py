import pandas as pd

df = pd.read_csv("sample.csv")
total = df["金額"].sum()
print(f"合計金額: {total}円")

import pandas as pd

# CSVを読み込む
df = pd.read_csv("sample.csv")

# 合計を計算
total = df["金額"].sum()
print(f"合計金額: {total}円")

# 結果をExcelに出力
df.to_excel("結果.xlsx", index=False)
print("結果.xlsx を作成しました")