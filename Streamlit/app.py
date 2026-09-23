import streamlit as st
import pandas as pd
import numpy as np
#title of the application
st.title("Jai shree Krishna")
#Display the simple text
st.write("This is simple input")
#create a simple dataframe
df = pd.DataFrame({
    'first column': [1, 2, 3, 4, 5, 6],
    'second column': [10, 20, 30, 40, 50, 60]
})
    
#display the dataframe
st.write("Here is the Dataframe")
st.write(df)
##create a line chart
chart_data=pd.DataFrame(
np.random.randn(20,3), columns=['a', 'b', 'c']
)
st.line_chart (chart_data)
