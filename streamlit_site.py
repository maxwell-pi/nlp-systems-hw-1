import streamlit as st

from notebook import Notebook

if 'nb' not in st.session_state:
    st.session_state.nb = Notebook()

nb = st.session_state.nb

st.title("Notebook")

search_term = st.text_input("Filter notes (make sure to press enter to apply filter):")

filtered_notes = nb.find(search_term) if search_term else nb.notes_dict

for title in filtered_notes:
    if st.button(title):
        content = nb[title]
        st.write(f"**{title}**")
        st.write(content)

st.markdown("---")
st.subheader("Write a new note:")

title = st.text_input("Title:")
body = st.text_area("Body:")

if st.button("Commit to notebook forever"):
    if title:
        try:
            nb[title] = body
            st.success("Note added successfully forever")
        except ValueError as e:
            st.error(str(e))
    else:
        st.error("A blank note is okay, but every note needs a name.")


