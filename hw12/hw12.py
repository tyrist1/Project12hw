import json

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    with open('settings.json') as f:
        settings = json.load(f)
    return render_template("index.html", **settings)
@app.route('/candidate/<id>')
def prof(id):
    with open('candidates.json') as f:
        candidates = json.load(f)
    for candidate in candidates:
        if candidate[id] == int(id):
            return render_template("candidate.html", **candidate)

if __name__=="__main__":
    app.run()