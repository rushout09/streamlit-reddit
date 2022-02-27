import streamlit as st
from google.cloud import firestore


class CreateNote:

    def __init__(self):
        self.db = firestore.Client.from_service_account_json(
    "./zone-3d684-firebase-adminsdk-z4pdn-9b6f2ac6d7.json")
        self.note = st.text_input("Write a note", key="note")
        self.tags = st.text_input("Enter Tags separated by space", key="tags")
        self.submit = st.button(label="Submit", on_click=self.post_note)

    def post_note(self):
        if self.note is not None and self.note.strip() != "":
            list_of_tags = []
            list_of_tags.extend(self.tags.split())
            doc_ref = self.db.collection("users").document('PZTEmq3SyocK4x00QwB1').collection('record')
            doc_ref.add({
                'note': self.note,
                'tags': list_of_tags,
                'modifiedAt': firestore.SERVER_TIMESTAMP
            })
            st.session_state["note"] = ""
            st.session_state["tags"] = ""



# collection_ref = db.collection("users").document('PZTEmq3SyocK4x00QwB1').collection('record')
#
# for doc in collection_ref.stream():
#     st.subheader(f"Title: {doc.to_dict()['title']}")
#     st.write(f":link: [{doc.to_dict()['url']}]({doc.to_dict()['url']})")