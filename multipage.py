import streamlit as st


class MultiPage:

    def __init__(self) -> None:
        self.pages = dict()

    def add_page(self, page_title, func) -> None:
        self.pages[page_title] = func

    def run(self):
        selected_page = st.sidebar.selectbox(
            'App Navigation',
            list(self.pages.keys())
        )
        self.pages[selected_page]()
