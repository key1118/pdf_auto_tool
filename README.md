# PDF自動処理ツール(AI要約、構造化、Excel出力)
このツールはpdfをアップロードするだけで、
AIが内容を**要約**し、日付•参加者•決定事項といった情報を**抽出**し、**Excel**にして出力するデモアプリです。

社内文書は議事録などの処理を効率化(自動化)できます。

## 主な機能
1. PDF -> テキスト抽出
pypdfを使ってPDFから自動でテキストを抽出します。

2. AI要約 
OpenAIのLLM(今回はgpt-4o-mini)を使用し、文書を短くわかりやすく要約します。

3. 情報抽出(構造化)
• 日付
• タイトル
• 参加者(複数可)
• 決定事項(複数可)
• 全体要約

4. Excel出力
構造化された情報を1行のExcelに出力します

## UIイメージ

## セットアップ
1. 仮想環境を作成

```python
python3 -m venv venv
source venv/bin/activate  
# Windows: venv\Scripts\activate
```

2. 必要ライブラリをインストール

```python
pip install -r requirements.txt
```

3. .env を作成
```python
OPENAI_API_KEY=あなたのAPIキー
```

## ファイル構成
pdf_auto_tool/
├── app.py                 # Streamlit UI
├── pdf_reader.py          # PDF → テキスト抽出
├── summarizer.py          # 要約生成
├── extractor.py           # 情報抽出（JSON）
├── excel_writer.py        # Excel 出力
├── sample.pdf             # デモ用PDF
├── requirements.txt
└── .env (自分で作成)

## 使用技術
•Python 3.x

•Streamlit

•pypdf

•pandas

•OpenAI API（gpt-4o-mini）

•openpyxl

•dotenv

## なぜこのツールを作ろうと思ったか
近年AIの出現により、様々な業務を自動化し、時間短縮&業務効率化へとつながっています。特に今回は

議事録の要点抽出、報告書の要約、決定事項の整理、情報のExcel転記

といった単純作業を自動化してみようと思いました。

この自動化により、

作業時間の削減、ミスの削減、情報整理の統一化

を実現できます。

## 今後拡張可能なアップデート
1. PDFフォーマット別の抽出精度向上
2. バッチ処理対応（複数PDFを一括処理）
3. RAGで検索性を強化

## 開発者
[小松慶太朗]

•Python / LLM / AI 自動化

•スクレイピング・情報抽出

•バックエンド開発

•企業向け業務効率化ツール構築

## お問い合わせ
AIを使った業務自動化ツールの開発も可能です。
お気軽にご連絡ください。

メールアドレス: kin29sasuke@outlook.com