import pandas as pd
from pathlib import Path

# dataフォルダの中のすべてのCSVを読み込む
folder = Path("data")
csv_files = list(folder.glob("*.csv"))

# 全部を1つの表にまとめる
dfs = []
for file in csv_files:
    df = pd.read_csv(file)
    dfs.append(df)

result = pd.concat(dfs, ignore_index=True)

# 合計を計算して表示
total = result["金額"].sum()
print(f"全体の合計金額: {total}円")
print(f"読み込んだファイル数: {len(csv_files)}")

total = result["金額"].sum()
average = result["金額"].mean()
print(f"全体の合計金額: {total}円")
print(f"平均金額: {average:.0f}円")
print(f"読み込んだファイル数: {len(csv_files)}")

# Excelに出力
result.to_excel("まとめ.xlsx", index=False)
print("まとめ.xlsx を作成しました")