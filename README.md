# NLP Systems HW 1
## Maxwell Pickering

## Structure and How-to-Run
The FastAPI API is found in `api.py`, and can be run `uvicorn api:app --reload`. The Flask app can be run `python app.py`. The Streamlit app can be run `streamlit run stream.py`.

The virtual environment can be reconstructed using `requirements.py` and Python 3.11.

The notebook logic is found in module `notebook.py`. The HTML templates for the Flask app's three page types are found in `templates`, while the CSS sheet for the Flask app is found at `static/style.css`. 

Notebook notes are stored in `history.json`; this is included to give some sample entries for evaluation. A sample note JSON scheme is included at `note.json` for evaluation.

## Notebook Documentation
The Notebook class is essentially a wrapper for a dictionary with title keys and note body values. However, on instantiation and on put operations, the state of the dictionary is loaded or saved in JSON format for the sake of persistence. The Notebook class is otherwise a diminished dictionary, not allowing deletions or updates to existing keys.

## API Documentation
- The root path allows only GET requests, returning a helper message of the form `{"message": "a helpful message"}.
- The `/list` path allows only GET requests, returning the full list of note titles, of the form {'note_list': ['title1', 'title2', ...]}
- The `/note/TITLE` paths allow only GET requests, returning the note associated with the given `TITLE`, of the form {'title': title, 'body': body}. If a title is given that does not match to a note, a 400 error is returned.
- The `/find?term=SEARCH_TERM` path allows only GET requests, and returns the list of note titles whose bodies contain the `SEARCH_TERM`, of the form {"term": term, "titles of matching note": ['title1', 'title2', ...]}
- The `/add` path allows for POST requests, accepting a `Note` object with JSON scheme `{'name': str, 'content': str}` and returning a confirmation message of the form `{'message': 'Note added successfully.', 'title': note.name, 'body': note.content}`. If a note with the same name already exists, a 400 error is returned.

## Flask and Streamlit sites
Once running, the Flask and Streamlit sites should be simple enough to operate without usage documentation.