import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("My First Streamlit App")
st.write("Hello")
st.text("Let's Start")

name = st.text_input("Enter name :")

if st.button("Submit"):
    st.success(f"Hello, {name}")

df = pd.DataFrame(np.random.randn(10, 2), columns=['A', 'B'])
st.line_chart(df)
st.bar_chart(df)

st.sidebar.title("Navigation")
st.sidebar.image("cr.jpg", caption="Ghost Image")

st.subheader("Upload CSV File")
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("This is **bold** text, this is *italic* text, and this is `code` text.")
st.code("for i in range(5):\n    print(i)", language='python')

text_name = st.text_input("What is your name")
text = st.text_area("Write something...")
number = st.number_input("Pick a number", min_value=0, max_value=100)
slider = st.slider("Select a value", 0, 100)
option = st.selectbox("Choose one", ["Option 1", "Option 2", "Option 3"])
multi = st.multiselect("Select multiple", ["A", "B", "C", "D"])
radio = st.radio("Pick one", ["Yes", "No"])
agree = st.checkbox("I agree to the items")

if st.button("Submit", key="submit2"):
    st.write("Name:", text_name)
    st.write("Text:", text)
    st.write("Number:", number)
    st.write("Slider:", slider)
    st.write("Option:", option)
    st.write("Multiple:", multi)
    st.write("Radio:", radio)
    st.write("Agreed:", agree)

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
st.pyplot(fig)
