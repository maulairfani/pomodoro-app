import pandas as pd
import streamlit as st

df = pd.read_csv('data.csv')
baru = [st.text_input('mk')]
baru = pd.Series(baru)
df['matkul'] = df['matkul'].append(baru)
# df.to_csv('data.csv')
st.table(df)
