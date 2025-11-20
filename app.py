import streamlit as st
from pdf_reader import extract_text_from_pdf
from summarizer import summarize_text
from extractor import extract_info
from excel_writer import json_to_excel

st.title("PDF 自動処理デモツール")
st.write("PDFをアップロードすると、要約・情報抽出・Excel出力を自動で行います。")

uploaded_file = st.file_uploader("PDFを選択してください", type=["pdf"])

if uploaded_file is not None:
    # 一時保存
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.info("PDFを読み込み中...")

    # PDF抽出
    try:
        text = extract_text_from_pdf("temp.pdf")
        st.success("PDFからテキスト抽出成功")
    except Exception as e:
        st.error(f"PDF抽出でエラー: {e}")
        st.stop()

    # 要約
    st.subheader("要約")
    try:
        summary = summarize_text(text)
        st.write(summary)
    except Exception as e:
        st.error(f"要約生成でエラー: {e}")

    # JSON抽出
    st.subheader("構造化情報（JSON）")
    try:
        info = extract_info(text)
        st.json(info)
    except Exception as e:
        st.error(f"情報抽出でエラー: {e}")
        st.stop()

    # Excel出力
    st.subheader("Excel 出力")
    try:
        path = json_to_excel(info, "result.xlsx")
        with open(path, "rb") as f:
            st.download_button(
                label="Excel をダウンロード",
                data=f,
                file_name="result.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        st.success("Excel 出力完了")
    except Exception as e:
        st.error(f"Excel 出力でエラー: {e}")
