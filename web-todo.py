import streamlit as st
import todo_utils_web

todos = todo_utils_web.get_todos()


def add_todo():
    new_todo = f"{st.session_state['todo']}\n"
    if new_todo != "":
        todos.append(new_todo)
        todo_utils_web.update_todos(todos)
    st.session_state["todo"] = ""


st.title("My Todo App")
st.subheader("This is the todo app.")
st.write("This app will help you to priorities your work.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        todo_utils_web.update_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo...", key="todo", on_change=add_todo)
