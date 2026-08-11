# Josh Dev PH

A minimal Flask portfolio inspired by the clean section-driven presentation of Python Philippines, refactored for a personal portfolio.

## Stack
- Python + Flask
- Jinja templates
- Plain CSS
- No database
- No JavaScript framework
- No Tailwind / Node build step

## Pages
- `/` Home
- `/about` About
- `/projects` Projects
- `/learn` Learn / YouTube resources
- `/contact` Contact / socials

## Reusable components
- `templates/base.html` — shared layout
- `templates/components/navbar.html`
- `templates/components/footer.html`
- `templates/components/macros.html`
  - `button(...)`
  - `content_card(...)` for projects and YouTube videos
  - `social_card(...)`

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

## Customize first
1. Update project, learning, and social data in `data/site_data.json`.
2. Replace `static/files/resume.pdf` with your actual resume.
3. Adjust copy in `templates/about.html`.
4. Add your real GitHub, LinkedIn, YouTube, and email URLs.
5. Optional: add image thumbnails to the reusable card macro later without changing page architecture.

## Managing site content

All repeatable content is stored in `data/site_data.json`. The file has three arrays:

- `projects` — cards shown on the Projects page; the first three also appear on Home.
- `learning` — cards shown on the Learn page.
- `socials` — links shown on the Contact page.

To add content, copy an existing object in the appropriate array, update its values, and keep the JSON syntax valid. Flask reads the file on every page request, so a browser refresh displays newly added items without Python or template changes.

Project and learning cards use `title`, `description`, `tags`, `url`, and `cta`. Social links use `name`, `handle`, and `url`.
