import streamlit as st
import function 

todos = function.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo) 
    function.write_todos(todos)


st.title("My  Todo")
st.subheader("This is my to-do app")
st.write("To increase productivity")
st.header('This is a header', divider= 'grey')

for todo in todos:
    st.checkbox(todo)
    
st.text_input(label="Todo input box",label_visibility= 'hidden', placeholder='Add a new todo..', on_change= add_todo, key='new_todo')