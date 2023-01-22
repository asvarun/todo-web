import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    todos.append(todo_local)
    functions.write_todos(todos)


st.title("To-Do Web App")
st.subheader("This is my todo web app")
st.write("This app increases productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key="new_todo")

