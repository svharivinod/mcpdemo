![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green)
![OpenAI](https://img.shields.io/badge/OpenAI-API-enabled-ff69b4)
![Playwright](https://img.shields.io/badge/Playwright-enabled-yellow)

# 🤖 MCP Demo — AI Chat Agent with Tool Use

This project is a command-line chatbot that integrates:

- 🧠 OpenAI's `gpt-4o-mini` for natural conversation
- 🌐 Google Search via a custom Playwright tool
- 🧰 Additional tools via MCP (Multi-Command Plugin) like DuckDuckGo, Airbnb, etc.

It allows queries like:

> **Search g-search for "top AI trends in 2025"**  
> **Use Playwright to open example.com and extract the heading**

---

## 📁 Project Structure

mcpdemo/
├── app.py # Main chat logic
├── main.py # Optional entry point
├── browser_mcp.json # MCP tool config
├── tools/
│ └── google-search/
│ └── server.js # Custom Google scraper with Playwright
├── .env # OpenAI key (ignored)
├── .gitignore
├── README.md
├── requirements.txt # Python dependencies
├── package.json # Node dependencies
└── pyproject.toml

---

## 🚀 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/svharivinod/mcpdemo.git
cd mcpdemo

2. Set up Python environment
Ensure you're using Python 3.11+

bash
Copy
Edit
python -m venv .venv
.venv\Scripts\activate     # Windows
# source .venv/bin/activate  # macOS/Linux
Install Python dependencies:

bash
Copy
Edit
uv pip install -r requirements.txt
# or use pip directly if not using uv
3. Install Node + Playwright
bash
Copy
Edit
npm install
npx playwright install
4. Add your OpenAI API key
Create a file named .env in the root directory:

ini
Copy
Edit
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
✅ This file is .gitignored and won't be pushed to GitHub.

🧪 How to Run
Start the chat:

bash
Copy
Edit
uv run app.py
You'll see:

pgsql
Copy
Edit
======== Interactive MCP Chat ========
Type 'exit' to end the chat.
Type 'clear' to clear the memory.
💬 Example Prompts to Try
Search g-search for "best AI tools in 2025"

Use Playwright to extract the heading from https://example.com

Search DuckDuckGo for news on generative AI

Exit → quit chat

Clear → clear memory context

🛡️ Security Note
API keys should never be committed. This repo blocks .env via .gitignore.

GitHub may reject pushes with secrets. If that happens, follow these steps to clean your Git history.

📄 License
MIT © svharivinod

yaml
Copy
Edit

