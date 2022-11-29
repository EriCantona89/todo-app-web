import streamlit
import functions

todos = functions.get_todos()


def add_todo():
    todo = streamlit.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)



streamlit.title('Todo App')
streamlit.subheader('This is my to do app')
streamlit.write('This is up is to incrase your productivy')


for index, todo in enumerate(todos):
    checkbox = streamlit.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del streamlit.session_state[todo]
        streamlit._rerun()

streamlit.text_input(label="Enter a todo", placeholder='Add new todo...',
                     on_change=add_todo, key='new_todo')

