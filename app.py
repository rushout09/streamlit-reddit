import streamlit as st
from multipage import MultiPage
from pages import create_note, list_note

app = MultiPage()

st.title('Zone App')

app.add_page("Create Note", create_note.CreateNote)
app.add_page("List Note", list_note.ListNote)

app.run()
