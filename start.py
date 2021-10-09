import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit')

"""
# Streamlit
## My first app
Here's our first attempt at using data to create a table:
"""

timeline = pd.read_excel("timeline.xlsx", index_col=0)

# Use checkboxes to show/hide data
if st.checkbox("Show data"):
    timeline

st.line_chart(timeline)