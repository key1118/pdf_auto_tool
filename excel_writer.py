# excel_writer.py

import pandas as pd

def json_to_excel(data: dict, output_path: str = "output.xlsx"):
    """
    JSON(dict) 形式の抽出結果を Excel に出力する関数。
    配列はカンマ区切りの文字列に変換して保存する。
    """

    # Excel が扱いやすいように加工
    flat_data = {}
    for key, value in data.items():
        if isinstance(value, list):
            flat_data[key] = ", ".join([str(v) for v in value])
        else:
            flat_data[key] = value

    df = pd.DataFrame([flat_data])  # 1行のテーブルにする

    try:
        df.to_excel(output_path, index=False)
    except Exception as e:
        raise RuntimeError(f"Excel 出力でエラー: {e}")

    return output_path
