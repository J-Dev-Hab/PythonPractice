import pandas as pd
from pathlib import Path
from datetime import datetime

# dataフォルダの中のすべてのCSVを読み込む
folder = Path("data")
csv_files = list(folder.glob("*.csv"))

# 全部を1つの表にまとめる
dfs = []
for file in csv_files:
    df = pd.read_csv(file)
    dfs.append(df)

result = pd.concat(dfs, ignore_index=True)

# 全体の合計・平均
total = result["金額"].sum()
average = result["金額"].mean()
print(f"全体の合計金額: {total}円")
print(f"平均金額: {average:.0f}円")
print(f"読み込んだファイル数: {len(csv_files)}")
print(f"処理した行数: {len(result)}行")

# 商品ごとの合計
product_total = result.groupby("商品")["金額"].sum()
print("\n【商品ごとの合計】")
print(product_total)

# Excelに出力（全体 + 商品ごと）
today = datetime.now().strftime("%Y%m%d")
output_path = Path("output") / f"まとめ_{today}.xlsx"

with pd.ExcelWriter(output_path) as writer:
    result.to_excel(writer, sheet_name="全体", index=False)
    product_total.to_excel(writer, sheet_name="商品ごと")

print(f"\n{output_path} を作成しました")