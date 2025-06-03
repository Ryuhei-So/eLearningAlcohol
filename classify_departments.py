import pandas as pd
import openai
from tqdm import tqdm
import os

def create_classification_mapping(df):
    unique_depts = df['所属(部署)'].unique()
    mapping = {}
    
    for dept in tqdm(unique_depts):
        if pd.isna(dept):
            mapping[dept] = "その他"
            continue
            
        if "精神" in str(dept):
            mapping[dept] = "精神科"
        elif "内科" in str(dept):
            mapping[dept] = "内科"
        else:
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{
                        "role": "user",
                        "content": f"以下の部署名を「精神科」「内科」「その他」のいずれかに分類してください。回答は分類のみ: {dept}"
                    }],
                    temperature=0.0
                )
                mapping[dept] = response.choices[0].message.content
            except Exception as e:
                print(f"Error classifying {dept}: {str(e)}")
                mapping[dept] = "その他"
    
    return mapping

def main():
    df = pd.read_excel("eLearning_data_250409.xlsx")
    print("部署名の分類を開始します...")
    mapping = create_classification_mapping(df)
    df['分類結果'] = df['所属(部署)'].map(mapping)
    
    output_file = "classified_eLearning_data.xlsx"
    df.to_excel(output_file, index=False)
    print(f"分類結果を {output_file} に保存しました")

if __name__ == "__main__":
    main()