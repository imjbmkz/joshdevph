from flask import Flask, render_template

app = Flask(__name__)

PROJECTS = [
    {
        "title": "Data Engineering Project",
        "description": "A featured data engineering project. Replace this copy with the problem, architecture, and measurable outcome.",
        "tags": ["Python", "SQL", "ETL"],
        "url": "https://github.com/",
        "cta": "VIEW PROJECT",
    },
    {
        "title": "Analytics & BI Project",
        "description": "Showcase a dashboard, semantic model, warehouse, or reporting modernization project here.",
        "tags": ["Power BI", "Analytics", "Data Modeling"],
        "url": "https://github.com/",
        "cta": "VIEW PROJECT",
    },
    {
        "title": "Automation Project",
        "description": "Highlight an API integration, workflow automation, or productivity tool you built.",
        "tags": ["Python", "API", "Automation"],
        "url": "https://github.com/",
        "cta": "VIEW PROJECT",
    },
]

LEARNING = [
    {
        "title": "Data Engineering Tutorial",
        "description": "A YouTube lesson or walkthrough. Replace with your actual video title and short learning outcome.",
        "tags": ["YouTube", "Data Engineering"],
        "url": "https://youtube.com/",
        "cta": "WATCH VIDEO",
    },
    {
        "title": "Analytics Explained",
        "description": "Use the same reusable content card for learning resources and videos.",
        "tags": ["YouTube", "Analytics"],
        "url": "https://youtube.com/",
        "cta": "WATCH VIDEO",
    },
]

SOCIALS = [
    {"name": "GitHub", "handle": "@your-github", "url": "https://github.com/"},
    {"name": "LinkedIn", "handle": "Josh Valdeleon", "url": "https://linkedin.com/"},
    {"name": "YouTube", "handle": "Josh Dev PH", "url": "https://youtube.com/"},
    {"name": "Email", "handle": "your@email.com", "url": "mailto:your@email.com"},
]


@app.route("/")
def home():
    return render_template("home.html", projects=PROJECTS[:3])


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/projects")
def projects():
    return render_template("projects.html", projects=PROJECTS)


@app.route("/learn")
def learn():
    return render_template("learn.html", items=LEARNING)


@app.route("/contact")
def contact():
    return render_template("contact.html", socials=SOCIALS)


if __name__ == "__main__":
    app.run(debug=True)
