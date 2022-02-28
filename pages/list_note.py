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
                result_dict = result.to_dict()

                cols = st.columns(4)
                tags = ''
                for tag in result_dict['tags']:
                    tags = tags + tag + ' '

                with st.form(key=result_dict['modifiedAt'].strftime("%b %d %Y %H:%M:%S")):
                    st.write(result_dict['modifiedAt'].strftime("%b %d %Y %H:%M:%S"))
                    note = st.text_area(label='note', value=result_dict['note'])
                    tags = st.text_input(label='tags', value=tags)
                    kwargs = {
                        'note': note,
                        'tags': tags,
                        'note_id': result.id
                    }
                    print(f"note1: {note}")
                    print(f"tags2: {tags}")
                    st.form_submit_button(label="Update", on_click=self.update_note,
                                   kwargs=kwargs)

    def list_note(self):
        print(f"Search Tags: {self.search_tags}")
        list_of_tags = []
        list_of_tags.extend(self.search_tags.split())
        print(f"List of tags: {list_of_tags}")
        doc_ref = self.db.collection("users").document('PZTEmq3SyocK4x00QwB1').collection('record')
        if len(list_of_tags) > 0:
            st.session_state['results'] = doc_ref.where('tags', 'array_contains_any', list_of_tags)\
                .order_by('modifiedAt', direction='DESCENDING').stream()

    def update_note(self, **kwargs):
        note = kwargs['note']
        tags = kwargs['tags']
        note_id = kwargs['note_id']
        print(f"note: {note}")
        print(f"tags: {tags}")
        if note is not None and note.strip() != "":
            list_of_tags = []
            list_of_tags.extend(tags.split())
            doc_ref = self.db.collection("users").document('PZTEmq3SyocK4x00QwB1')\
                .collection('record').document(note_id)
            doc_ref.set({
                'note': note,
                'tags': list_of_tags,
                'modifiedAt': firestore.SERVER_TIMESTAMP
            })
# collection_ref = db.collection("users").document('PZTEmq3SyocK4x00QwB1').collection('record')
#
# for doc in collection_ref.stream():
#     st.subheader(f"Title: {doc.to_dict()['title']}")
#     st.write(f":link: [{doc.to_dict()['url']}]({doc.to_dict()['url']})")