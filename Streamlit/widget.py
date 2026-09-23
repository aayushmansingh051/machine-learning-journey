import streamlit as st
import pandas as pd
st.title("Streamlit Text input")
#Display
name=st.text_input("Eneter your name: ")
st.write(f"Hello,{name}")
age=st.slider("select your age", 0,100,25)
st.write(f"age is:,{age}")

#choice to select
options = ["Python", "Java", "C++", "JavaScript"]
choice= st.selectbox("Choose your favorite language:", options)
st.write(f"You selected {choice}.")
#upload the doc
uploaded_file=st.file_uploader("choose a csv file",type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)
