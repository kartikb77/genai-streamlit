import streamlit as st
import pandas as pd
import numpy as np


st.title("My First streamlit app")
st.write("Hello")
st.text("Let's Start")

name = st.text_input("Enter name :")

if st.button("Submit"):
    st.success(f"Hello, {name}")

df = pd.DataFrame(np.random.randn(10, 2), columns=['A', 'B'])

st.line_chart(df)
st.bar_chart(df)

st.sidebar.title("Navigation")

st.sidebar.image("/Users/kartikborekar77/Downloads/cr.jpg", caption="Ghost Image")

st.subheader("Upload CSV File")

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    
#text markdown formatting
st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("This is **bold** text, this is *italic* text, and this is `code` text[http://streamlit.io].")
st.code("for i in range(5):\n    print(i)", language='python')

st.text_input("What is your name")
st.text_area("Write something...")
st.number_input("Pick a number", min_value=0, max_value=100)
st.slider("Select a value", 0, 100)
st.selectbox("Choose one", ["Option 1", "Option 2", "Option 3"])
st.multiselect("Select multiple", ["A", "B", "C", "D"])
st.radio("Pick one", ["Yes", "No"])
st.checkbox("I agree to the items")

if st.button("Submit", key="submit2"):
    st.write("Name:", name)
    st.write("Text:", text)
    st.write("Number:", number)
    st.write("Slider:", slider)
    st.write("Option:", option)
    st.write("Multiple:", multi)
    st.write("Radio:", radio)

import streamlit as st
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])

st.pyplot(fig)

