import pandas as pd
import openai
from tqdm import tqdm
import os

def enhanced_classify(row):
    # 基本情報を結合（欠損値処理済み）
    context = f"""
    部署: {str(row['所属(部署)']) if pd.notna(row['所属(部署)']) else '未記載'}
    学会: {str(row.get('所属学会', '')) if pd.notna(row.get('所属学会', '')) else '未記載'} 
    勤務先: {str(row.get('勤務先名称', '')) if pd.notna(row.get('勤務先名称', '')) else '未記載'}
    """
    
    # 拡張キーワードチェック
    keywords = {
        '精神科': ['精神', 'メンタル', '認知症', 'psych', 'mental'],
        '内科': ['内科', '消化器', '循環器', '呼吸器', '内分泌', '糖尿病', '肝臓']
    }
    
    for category, terms in keywords.items():
        if any(term in context for term in terms):
            return category
            
    # LLM分類（追加情報を含む）
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "system",
                "content": "医療機関の分類を行ってください。回答は「精神科」「内科」「その他」のいずれかで。"
            },{
                "role": "user",
                "content": f"以下の情報を分類してください:\n{context}"
            }],
            temperature=0.1
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"分類エラー: {str(e)}")
        return "その他"

def main():
    # データ読み込み（前回結果含む）
    df = pd.read_excel("classified_eLearning_data.xlsx")
    
    # 進捗表示付きで分類実行
    print("拡張分類を開始します...")
    tqdm.pandas(desc="処理中")
    df['分類結果2'] = df.progress_apply(enhanced_classify, axis=1)
    
    # 新旧分類の一致率を計算
    match_rate = (df['分類結果'] == df['分類結果2']).mean()
    print(f"\n新旧分類一致率: {match_rate:.1%}")
    
    # 結果保存（新しいファイルに）
    output_path = "reclassified_eLearning_data.xlsx"
    df.to_excel(output_path, index=False)
    print(f"\n結果を {output_path} に保存しました")

if __name__ == "__main__":
    main()
