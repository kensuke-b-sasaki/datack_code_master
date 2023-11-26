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

st.title("Drug code search")


# CSVファイルのパス
drug_file_path = 'm_drug.csv'

# CSVファイルが存在するか確認
if not os.path.exists(drug_file_path):
    st.error(f"ファイル '{drug_file_path}' が見つかりません。")

# CSVファイルを読み込む
df_drug = pd.read_csv(drug_file_path)

# 上部に入力欄を追加
st.header("Datack Code Master")

drug_name_options = st.multiselect("薬剤名を入力", options=df_drug['一般名'].unique())
atccode_options = st.multiselect("ATCコードを入力", options=df_drug['atccode_who'].unique())

# データフィルタリングとテーブルの表示
if drug_name_options or atccode_options:
    filtered_df = df_drug[df_drug['一般名'].isin(drug_name_options) | df_drug['atccode_who'].isin(atccode_options)]

    # テーブルの表示
    st.write("Code list")
    st.dataframe(filtered_df)

    # CSVダウンロード
    st.download_button(
        label="Download CSV",
        data=filtered_df.to_csv(index=False),
        file_name='filtered_drugs.csv',
        mime='text/csv'
    )