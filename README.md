# BrandOS AKIJ Render Ready

## Render Settings

Build:
pip install -r requirements.txt

Start:
gunicorn --chdir api index:app

Upload this folder directly to GitHub.

Structure:

api/
  __init__.py
  index.py

public/
  index.html

database/
  sample.json
