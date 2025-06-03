# eLearningAlcohol - 医療従事者部署分類プロジェト

医療従事者のeLearningデータを部署・診療科別に自動分類するPythonプロジェクトです。

## 概要

このプロジェクトは、医療従事者の所属部署情報を基に、以下の診療科カテゴリに自動分類します：
- 精神科
- 内科  
- 外科
- 小児科
- 産婦人科
- 眼科
- 耳鼻咽喉科
- 整形外科
- 皮膚科
- 泌尿器科
- 脳神経外科
- その他

## ファイル構成

### データファイル
- `eLearning_data_250409.xlsx` - 元データ
- `classified_eLearning_data.xlsx` - 初回分類結果
- `reclassified_eLearning_data.xlsx` - 最終分類結果

### スクリプトファイル
- `classify_departments.py` - OpenAI APIを使用した部署分類
- `reclassify_departments.py` - キーワードマッチングによる再分類
- `reclassify_department1.py` - 追加分類ロジック
- `reclassify_departments_ai.py` - AI支援分類

### レポートファイル
- `report.Rmd` / `report.html` - 分析レポート
- `report2.Rmd` / `report2.html` - 追加分析レポート

### その他
- `japan.geojson` - 日本地図データ
- `作業記録.md` - 作業履歴

## 使用方法

### 1. 環境準備
```bash
pip install pandas openai tqdm openpyxl
```

### 2. OpenAI API設定
```bash
export OPENAI_API_KEY="your-api-key"
```

### 3. 分類実行
```bash
python classify_departments.py
```

## 分類ロジック

1. **キーワードマッチング**: 部署名に含まれるキーワードで一次分類
2. **AI分類**: 不明な部署はOpenAI APIで分類
3. **追加情報活用**: 所属学会・勤務先名称も考慮して精度向上

## 実行結果

- 処理対象: 58ユニーク部署名
- 処理時間: 約45-72秒
- 分類精度: 85.3%の一致率
- エラー率: 0%

## 注意事項

- OpenAI APIキーの設定が必要
- Python 3.x環境での実行を推奨
- 大量データ処理時はAPI使用量にご注意ください