import streamlit as st
import pandas as pd
import os

# アプリのページ設定
st.set_page_config(
     page_title="Code Master",
     page_icon=":search:",
     initial_sidebar_state="expanded",
)

st.markdown("# Welcome to Code Master")
st.sidebar.success("Select a page above.")
