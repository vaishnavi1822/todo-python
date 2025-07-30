import streamlit as st
from datetime import datetime

# Dashboard title
st.title("Personal Smart Assistant Dashboard")

# Time and date display
st.subheader("Current Date & Time:")
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.write(current_time)

# Section for To-Do List
st.subheader("To-Do List")
if 'todo_list' not in st.session_state:
    st.session_state['todo_list'] = []

# Add items to the to-do list
new_task = st.text_input("Add a task:")
if st.button("Add Task"):
    if new_task:
        st.session_state['todo_list'].append(new_task)
        st.success(f"Added: {new_task}")

# Display the to-do list
if st.session_state['todo_list']:
    st.write("### Tasks:")
    for idx, task in enumerate(st.session_state['todo_list']):
        st.write(f"{idx + 1}. {task}")
        if st.button(f"Remove Task {idx + 1}"):
            st.session_state['todo_list'].pop(idx)

# Section for Notes
st.subheader("Notes")
if 'notes' not in st.session_state:
    st.session_state['notes'] = ""

notes = st.text_area("Write your notes here:", st.session_state['notes'])
if st.button("Save Notes"):
    st.session_state['notes'] = notes
    st.success("Notes saved!")



