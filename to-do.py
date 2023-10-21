import streamlit as st
import function 

todos = function.get_todos()

st.title("My  Todo")
st.subheader("This is my to-do app")
st.write("To increase productivity")
# st.header('This is a header', divider= 'grey')

for todo in todos:
    st.checkbox(todo)
    
st.text_input(label="",placeholder='Add a new todo..')