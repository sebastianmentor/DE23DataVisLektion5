import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(30, 5), columns=["a", "b", "c","d", "e"])

st.bar_chart(chart_data)

st.write(chart_data)