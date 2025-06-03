import pandas as pd

# Excelファイルの読み込み
file_path = "reclassified_eLearning_data.xlsx"
df = pd.read_excel(file_path)

# 分類結果3列を追加
df["分類結果3"] = df["分類結果2"]  # まずは分類結果2をコピー

# その他ケースの処理
for index, row in df.iterrows():
    if row["分類結果2"] == "その他":
        info = f"{row['所属学会']} {row['勤務先名称']} {row['所属(部署)']}".lower()
        
        # キーワードに基づく分類ロジック
        if "外科" in info:
            df.at[index, "分類結果3"] = "外科"
        elif "小児科" in info:
            df.at[index, "分類結果3"] = "小児科"
        elif "産婦人科" in info or "産科" in info or "婦人科" in info:
            df.at[index, "分類結果3"] = "産婦人科"
        elif "眼科" in info:
            df.at[index, "分類結果3"] = "眼科"
        elif "耳鼻咽喉科" in info or "耳鼻科" in info:
            df.at[index, "分類結果3"] = "耳鼻咽喉科"
        elif "整形外科" in info:
            df.at[index, "分類結果3"] = "整形外科"
        elif "皮膚科" in info:
            df.at[index, "分類結果3"] = "皮膚科"
        elif "泌尿器科" in info:
            df.at[index, "分類結果3"] = "泌尿器科"
        elif "脳外科" in info or "神経外科" in info:
            df.at[index, "分類結果3"] = "脳神経外科"
        elif "精神科" in info or "心療内科" in info:
            df.at[index, "分類結果3"] = "精神科"
        elif "内科" in info:
            df.at[index, "分類結果3"] = "内科"
        else:
            df.at[index, "分類結果3"] = "その他"  # 不明な場合はそのまま

# Excelファイルに保存
with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    df.to_excel(writer, index=False, sheet_name='Sheet1')

print("分類結果3の追加と更新が完了しました。")