import streamlit as st
import functions

todos = functions.get_todos()

st.title("To-Do Web App")
st.subheader("This is my todo web app")
st.write("This app increases productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")

