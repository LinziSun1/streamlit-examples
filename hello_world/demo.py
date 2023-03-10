import streamlit as st
import pandas as pd
import numpy as np
# markdown
st.markdown('Streamlit Demo')

# 设置网页标题
st.title('streamlit')


st.header('Table')

st.text('Table example')
code2 = '''df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('row %d' % (i+1) for i in range(5))
)

st.table(df)'''
st.code(code2, language='python')



df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('row %d' % (i+1) for i in range(5))
)

st.table(df)

st.header('Chart')

st.text('Chart example')
code2 = '''chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)'''
st.code(code2, language='python')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.header('Map')

st.text('Map example')
code2 = '''df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(df)'''
st.code(code2, language='python')

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(df)


