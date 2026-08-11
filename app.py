import json
from pathlib import Path

from flask import Flask, render_template

app = Flask(__name__)
DATA_FILE = Path(app.root_path) / "data" / "site_data.json"


def load_site_data():
    """Load editable site content on every request so JSON updates appear immediately."""
    with DATA_FILE.open(encoding="utf-8") as data_file:
        data = json.load(data_file)

    for collection in ("projects", "learning", "socials"):
        if not isinstance(data.get(collection), list):
            raise ValueError(f'"{collection}" must be a JSON array in {DATA_FILE}')

    return data


@app.route("/")
def home():
    data = load_site_data()
    return render_template("home.html", projects=data["projects"][:3])


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/projects")
def projects():
    data = load_site_data()
    return render_template("projects.html", projects=data["projects"])


@app.route("/learn")
def learn():
    data = load_site_data()
    return render_template("learn.html", items=data["learning"])


@app.route("/contact")
def contact():
    data = load_site_data()
    return render_template("contact.html", socials=data["socials"])


if __name__ == "__main__":
    app.run(debug=True)
