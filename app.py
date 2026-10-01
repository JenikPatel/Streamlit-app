import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello World")

x = st.slider('x')
st.write(x, 'square is', x * x)

df = pd.DataFrame(np.random.randn(10, 20),
                  columns = ("col %d" %i for i in range(20)))
st.dataframe(df.style.highlight_max(axis = 0))

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.16, -122.4],
    columns = ['lat', 'lon']
    )
st.map(map_data)

map_data_2 = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50]  + [22.55, 72.95],
    columns = ['lat', 'lon']
)
st.map(map_data_2)

if "counter" not in st.session_state:
    st.session_state.counter = 0
st.session_state.counter += 1
st.header(f"You have run this page for {st.session_state.counter}")
st.button("Run again")