# RAI Chatbot (Flask)

A minimal Flask scaffold for a chatbot web UI suitable for local development and Azure deployment.

Folder layout

rai-chatbot/

- `app.py` — main Flask app with a / and /chat endpoint
- `requirements.txt` — Python dependencies
- `templates/index.html` — chat UI
- `static/style.css`, `static/script.js` — client assets
- `.venv/` — optional virtual environment (add to `.gitignore`)

Quick start (PowerShell)

```powershell
cd c:\Users\nalla\Desktop\ai\rai-chatbot
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
# Run the app
python app.py
# Then open http://localhost:5000 in your browser
```

Notes for Azure

- To deploy to Azure App Service: create the app, push this repo, set the `WEBSITES_PORT` or `PORT` app setting if needed, and use a `requirements.txt` for install.
- To deploy as a container: add a `Dockerfile` and containerize your app.
- For Azure OpenAI integration: add `azure-ai-openai` (or Azure-compatible SDK), store keys in Azure KeyVault / App Settings, and replace the placeholder in `app.py` with actual API calls.

Next steps (optional)

- Add authentication, rate limiting and error logging
- Replace placeholder reply in `app.py` with a call to Azure OpenAI or your bot backend
- Add CI/CD workflow for Azure deployment
