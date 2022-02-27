import streamlit as st
from google.cloud import firestore


class ListNote:

    def __init__(self):
        if 'results' not in st.session_state:
            st.session_state['results'] = None
        self.db = firestore.Client.from_service_account_json(
    "./zone-3d684-firebase-adminsdk-z4pdn-9b6f2ac6d7.json")
        self.search_tags = st.text_input("Enter a tag to search notes", key="search_tags")
        self.submit = st.button(label="Submit", on_click=self.list_note)
        if st.session_state['results'] is not None:
            for result in st.session_state['results']:
                st.write(result.to_dict())

    def list_note(self):
        print(f"Search Tags: {self.search_tags}")
        list_of_tags = []
        list_of_tags.extend(self.search_tags.split())
        print(f"List of tags: {list_of_tags}")
        doc_ref = self.db.collection("users").document('PZTEmq3SyocK4x00QwB1').collection('record')
        if len(list_of_tags) > 0:
            st.session_state['results'] = doc_ref.where('tags', 'array_contains_any', list_of_tags)\
                .order_by('modifiedAt', direction='DESCENDING').stream()


# collection_ref = db.collection("users").document('PZTEmq3SyocK4x00QwB1').collection('record')
#
# for doc in collection_ref.stream():
#     st.subheader(f"Title: {doc.to_dict()['title']}")
#     st.write(f":link: [{doc.to_dict()['url']}]({doc.to_dict()['url']})")