# summarizer.py

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SUMMARY_PROMPT = """
以下の文書を読み、３~５行に簡潔に要約してください。
専門用語は噛み砕いて書いてください。
重要な日付・人物・決定事項があれば明記してください。

【入力文書】
{document}
"""

def summarize_text(document: str) -> str:
    """
    文書をLLMに要約させる関数。
    """
    try:
        prompt = SUMMARY_PROMPT.format(document=document)

        response = client.chat.completions.create(
            model="gpt-4o-mini",   # 軽くて早くて安い
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_completion_tokens=300,
        )

        summary = response.choices[0].message.content.strip()
        return summary

    except Exception as e:
        raise RuntimeError(f"要約生成でエラー: {e}")
