# extractor.py

import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

EXTRACT_PROMPT = """
以下の文書から指定した項目を抽出し、完全にJSON形式で返してください。
存在しない項目は空文字 "" を返してください。

抽出する項目:
- date（文書の日付）
- title（議事録のタイトル）
- participants（参加者の名前を配列で）
- decided_items（決定事項を箇条書きで配列）
- summary（文書全体の短い要約：2〜4行）

絶対にJSON以外の文字を返さないでください。

【文書】
{document}
"""

def extract_info(document: str) -> dict:
    """
    LLMを使って文書から情報を抽出し、JSON(dict)で返す関数。
    """
    try:
        prompt = EXTRACT_PROMPT.format(document=document)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_completion_tokens=500
        )

        raw_json = response.choices[0].message.content.strip()

        # JSONパース（エラー時の保険付き）
        try:
            data = json.loads(raw_json)
        except json.JSONDecodeError:
            # JSONが多少壊れてても直すチャレンジ
            fixed = raw_json.replace("```json", "").replace("```", "")
            data = json.loads(fixed)

        return data

    except Exception as e:
        raise RuntimeError(f"情報抽出でエラー: {e}")
