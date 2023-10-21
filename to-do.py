import streamlit as st
import function 

todos = function.get_todos()
dones = function.get_done_todos()
done_todo = ''

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo) 
    function.write_todos(todos)


st.title("My Todo")
# st.subheader("This is my to-do app")
# st.write("To increase productivity")
st.header('Add a Todo', divider= 'grey')
st.text_input(label="Todo input box", label_visibility= 'hidden', placeholder='Add a new todo..', on_change= add_todo, key='new_todo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        function.complete_todos(dones=todo)
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
        
st.header('Last 5 completed todos', divider= 'grey')
top5 = dones[-1:-6:-1]
for i in top5:
    st.write(i)
    
with st.expander("Click here to show all todos"):
    for done in dones:
        st.write(done)
    
