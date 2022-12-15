import pandas as pd
#import openpyxl
from glob import glob
import datetime
import time
import sys
args = sys.argv
import streamlit as st
from PIL import Image

st.title('指揮官能力値')

df = pd.read_csv('CAS.csv',encoding='shift_jis')

with st.form("my_form", clear_on_submit=False):
    heisyu = st.selectbox(label='兵種を選択してください', options=['全兵種','歩兵','騎兵','槍兵','弓兵'])
    ST = st.selectbox(label='ソート能力値選択', options=['信仰\nHPバフ','武勇\n攻撃バフ','知恵\nクリダメ','計略\n防御バフ','幸運\nクリ率'])
    submitted = st.form_submit_button("表示")

if submitted:
    with st.spinner("処理中です..."):
        time.sleep(1)
    if heisyu == '歩兵':
        df1 = df.query('兵種 == "歩"')
    elif heisyu == '騎兵':
        df1 = df.query('兵種 == "騎"') 
    elif heisyu == '槍兵':
        df1 = df.query('兵種 == "槍"')
    elif heisyu == '弓兵':
        df1 = df.query('兵種 == "弓"')
    else:
        df1 = df
    df2 = df1.sort_values(ST, ascending=False)
    st.dataframe(df2)
