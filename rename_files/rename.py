from pathlib import Path

# 対象のフォルダ
folder = Path(".")

# フォルダ内のすべてのファイルを取得
files = [f for f in folder.iterdir() if f.is_file() and f.name != "rename.py"]

print(f"対象ファイル数: {len(files)}")

for i, file in enumerate(files, start=1):
    # 新しい名前（例：file_001.txt）
    new_name = f"file_{i:03d}{file.suffix}"
    new_path = folder / new_name
    
    print(f"{file.name} → {new_name}")
    # 実際に名前を変える（最初はコメントアウトして確認だけでもOK）
    file.rename(new_path)

print("完了（名前変更はコメントアウト中）")