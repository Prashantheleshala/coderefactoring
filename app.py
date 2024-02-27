from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        if note and note.strip():
            notes.append(note.strip())
    return render_template("home.html", notes=notes)  

@app.route('/edit/<int:index>', methods=["POST"])
def edit(index):
    if request.method == "POST":
        updated_note = request.form.get("updated_note")
        if updated_note and updated_note.strip():
            notes[index] = updated_note.strip()
    return redirect(url_for('index'))

@app.route('/delete/<int:index>', methods=["POST"])
def delete(index):
    if request.method == "POST":
        del notes[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
