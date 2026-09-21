# AI Email Generator

This project creates professional emails using the Groq API. It works with Streamlit locally, with Streamlit Cloud, and in Google Colab.

## Files

- `app.py` – main app logic
- `requirements.txt` – project dependencies
- `.gitignore` – hides secret files from GitHub
- `.streamlit/secrets.toml` – local Streamlit secret file
- `.env` – local environment file for development

## 1) GitHub + Streamlit deployment

GitHub is only for storing the code. It does not run the app by itself.

To deploy from GitHub:

1. Push `app.py` and `requirements.txt` to a GitHub repository.
2. Open Streamlit Cloud.
3. Click “New app”.
4. Connect your GitHub account.
5. Choose your repository and branch.
6. Set the app file to `app.py`.
7. Add the secret in the Streamlit Cloud dashboard:

```toml
GROQ_API_KEY = "your_real_groq_api_key_here"
```

8. Deploy.

Important: do not upload your real API key to GitHub.

## 2) Local Streamlit setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.streamlit/secrets.toml`:

```toml
GROQ_API_KEY = "your_real_groq_api_key_here"
```

Run the app:

```bash
streamlit run app.py
```

## 3) Google Colab setup

### Step A: install libraries

```python
!pip install streamlit groq
```

### Step B: set the API key from Google Colab secrets

```python
from google.colab import userdata
import os

os.environ["GROQ_API_KEY"] = userdata.get("GROQ_API_KEY")
print("API key loaded:", bool(os.environ.get("GROQ_API_KEY")))
```

### Step C: run the app

```python
!streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

### Step D: expose it with Cloudflare (no ngrok or third-party API)

```python
!curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -o /usr/local/bin/cloudflared
!chmod +x /usr/local/bin/cloudflared
```

Then start the tunnel:

```python
!nohup cloudflared tunnel --url http://localhost:8501 > /tmp/cloudflared.log 2>&1 &
```

After a few seconds, check the tunnel log:

```python
!cat /tmp/cloudflared.log
```

This will show a Cloudflare URL that you can open in the browser.

## 4) Colab secret setup in Google Colab

From the Colab menu:

1. Click the key icon on the left sidebar.
2. Choose “Secrets”.
3. Add a new secret named:

```text
GROQ_API_KEY
```

4. Paste your actual Groq API key.
5. Use this code in notebook:

```python
from google.colab import userdata
import os

os.environ["GROQ_API_KEY"] = userdata.get("GROQ_API_KEY")
```

Then your app reads it using:

```python
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
```

## 5) Recommended app code for Groq

Use this part in `app.py`:

```python
import os
import streamlit as st
from groq import Groq

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

if not GROQ_API_KEY:
    try:
        GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    except Exception:
        GROQ_API_KEY = None

if not GROQ_API_KEY:
    st.error("GROQ_API_KEY was not found.")
    st.stop()

client = Groq(api_key=GROQ_API_KEY)
```

## 6) Secret file example

For local use:

```toml
GROQ_API_KEY = "your_real_key_here"
```

For environment variable use:

```bash
export GROQ_API_KEY="your_real_key_here"
```

## 7) Important security note

Never upload your key to GitHub.

This project ignores these files:

```gitignore
.streamlit/secrets.toml
.env
__pycache__/
*.pyc
```

## 8) Common commands summary

### Streamlit local

```bash
pip install -r requirements.txt
streamlit run app.py
```

### Colab + secrets

```python
from google.colab import userdata
import os
os.environ["GROQ_API_KEY"] = userdata.get("GROQ_API_KEY")
```

### Colab + Cloudflare tunnel

```python
!pip install streamlit groq
!curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -o /usr/local/bin/cloudflared
!chmod +x /usr/local/bin/cloudflared
!nohup streamlit run app.py --server.address 0.0.0.0 --server.port 8501 > /tmp/streamlit.log 2>&1 &
!nohup cloudflared tunnel --url http://localhost:8501 > /tmp/cloudflared.log 2>&1 &
```

## 9) Final note

Your app does not need any external AI API besides Groq. The only secret you need is the Groq API key.
