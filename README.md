# Post-job-AI-Assistant

PoC Streamlit app that extracts structured job fields from uploaded/pasted/URL job adverts using OpenAI.

This README explains how to deploy the app to Heroku and run it locally from the dev container (Ubuntu 24.04.2 LTS).

## Heroku deploy steps (CLI)
1. Commit your repo:
```sh
git add .
git commit -m "Prepare for Heroku"
```
2. Create Heroku app and push:
```sh
heroku create your-app-name
git push heroku main
```
3. Set required environment variable:
```sh
heroku config:set OPENAI_API_KEY="sk-..."
```
4. Scale and open:
```sh
heroku ps:scale web=1
heroku open
```
To open the app from the dev container host's default browser, use:
```sh
$BROWSER https://your-app-name.herokuapp.com
```
5. View logs:
```sh
heroku logs --tail
```

## Local testing (inside dev container)
Install deps and run locally:
```sh
pip install -r requirements.txt
streamlit run app.py
```
Open locally in host browser:
```sh
$BROWSER http://localhost:8501
```

## Notes
- The app expects the env var `OPENAI_API_KEY`.
- `python-docx` and `pypdf` are optional; include them only if you need DOCX/PDF parsing.
- If you use a different OpenAI SDK version, verify the client calls in `app.py`.
- This workspace runs in a dev container on Ubuntu 24.04.2 LTS. Use `$BROWSER <url>` to open pages in the host's default browser from the container.
