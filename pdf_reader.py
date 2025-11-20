# pdf_reader.py

from pypdf import PdfReader

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    PDFからテキストを抽出して1つの文字列として返す関数。
    LLMで扱いやすいように改行を整形する。
    """
    try:
        reader = PdfReader(pdf_path)
    except Exception as e:
        raise RuntimeError(f"PDFの読み込みに失敗しました: {e}")

    text = ""

    for page_num, page in enumerate(reader.pages):
        try:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        except Exception as e:
            print(f"ページ {page_num} の抽出でエラー: {e}")

    # LLMに食わせやすいよう軽く整形
    clean_text = text.replace("  ", " ").strip()

    if not clean_text:
        raise ValueError("PDFからテキストが抽出できませんでした。画像タイプのPDFの可能性があります。")

    return clean_text
