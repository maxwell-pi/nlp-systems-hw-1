from flask import Flask, render_template, request, redirect

from notebook import Notebook

app = Flask(__name__)
nb = Notebook()

@app.route('/')
def index():
    search_term = request.args.get('search') or ''
    return render_template('index.html', notes=nb.find(search_term), search_term=search_term)

@app.route('/note/<title>')
def view_note(title):
    if title in nb:
        return render_template('note.html', title=title, content=nb[title])
    return "No note with this title exists, sorry.", 404

@app.route('/add', methods=['GET', 'POST'])
def add_note():

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        nb[title] = body
        return redirect('/')
    
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
