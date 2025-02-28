from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from notebook import Notebook

nb = Notebook()
app = FastAPI()

class Note(BaseModel):
    name: str
    content: str

@app.get("/")
def root():
    return {'message': "Welcome to notebook API. Use /list to get notebook contents, use /find?term=YOUR_SEARCH_TERM to search, and use /note/TITLE to access a specific note."}

@app.get("/list")
def get_list():
    return {'note_list': list(nb.items())}

@app.get("/note/{title}")
def get_note(title: str):
    try:
        return {'title': title, 'body': nb[title]}
    except KeyError:
        raise HTTPException(status_code=400, detail=f'No note with title {title}.')

@app.get("/find")
def find(term: str):
    return {"term": term, "titles of matching note": nb.find(term)}

@app.post('/add')
def add(note: Note):
    try:
        nb[note.name] = note.content
    except ValueError:
        raise HTTPException(status_code=400, detail=f'Cannot overwrite pre-exisitng note with title {note.name}.')
    return {'message': 'Note added successfully.', 'title': note.name, 'body': note.content}
