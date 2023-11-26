import streamlit as st
import pandas as pd
import os

st.markdown(
    """
    <style>
        /* 入力欄の幅をページ幅いっぱいにする */
        .stTextInput > div > div > input {
            width: 100%;
        }
        /* テーブルの幅をページ幅いっぱいにする */
        .stDataFrame {
            width: 100%;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Disease code search")


# CSVファイルのパス
disease_file_path = 'm_disease.csv'

# CSVファイルが存在するか確認
if not os.path.exists(disease_file_path):
    st.error(f"ファイル '{disease_file_path}' が見つかりません。")

# CSVファイルを読み込む
df_disease = pd.read_csv(disease_file_path)

# 上部に入力欄を追加
st.header("Datack Code Master")

icd10_options = st.multiselect("ICD10コードを入力", options=df_disease['ICD10分類コード'].unique())
disease_code_options = st.multiselect("傷病名コードを入力", options=df_disease['傷病名コード'].unique())

# データフィルタリングとテーブルの表示
if icd10_options or disease_code_options:
    filtered_df = df_disease[df_disease['ICD10分類コード'].isin(icd10_options) | df_disease['傷病名コード'].isin(disease_code_options)]

    # テーブルの表示
    st.write("Code list")
    st.dataframe(filtered_df)

    # CSVダウンロード
    st.download_button(
        label="Download CSV",
        data=filtered_df.to_csv(index=False),
        file_name='filtered_disease.csv',
        mime='text/csv'
    )
