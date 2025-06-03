import pandas as pd
import openai
import os
from tqdm import tqdm

# OpenAI API設定
openai.api_key = os.getenv('OPENAI_API_KEY')

def classify_department(info):
    """OpenAI APIを使用して部署を分類"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "以下の情報から医師の専門科を分類してください。内科、精神科、外科、小児科、産婦人科、眼科、耳鼻咽喉科、整形外科、皮膚科、泌尿器科、脳神経外科、その他から選択してください。"},
                {"role": "user", "content": info}
            ],
            temperature=0.3,
            max_tokens=10
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"APIエラー: {e}")
        return "その他"

# Excelファイルの読み込み
file_path = "reclassified_eLearning_data.xlsx"
df = pd.read_excel(file_path)

# 分類結果3列を追加
df["分類結果3"] = df["分類結果2"]  # まずは分類結果2をコピー

# その他ケースの処理
for index, row in tqdm(df.iterrows(), total=len(df)):
    if row["分類結果2"] == "その他":
        info = f"所属学会: {row['所属学会']}, 勤務先名称: {row['勤務先名称']}, 所属部署: {row['所属(部署)']}"
        df.at[index, "分類結果3"] = classify_department(info)

# Excelファイルに保存
with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    df.to_excel(writer, index=False, sheet_name='Sheet1')

print("AIによる分類結果3の追加と更新が完了しました。")