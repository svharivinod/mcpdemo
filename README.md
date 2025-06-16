📘 mcpdemo — Multi-Tool Chat Agent (OpenAI + Playwright + MCP)
This is an AI-powered command-line chatbot that integrates:

✅ OpenAI Chat API

✅ Custom Google Search via Playwright

✅ Support for MCP (Multi-Command Plugin) tools like DuckDuckGo, Airbnb, etc.

It allows natural conversations and tool-augmented queries like:

1) Use Playwright to go to https://books.toscrape.com and list the titles and prices of the first 3 books.
2) Visit https://quotes.toscrape.com with Playwright and extract 3 quotes along with their authors.
3) Use Playwright to visit https://www.w3schools.com/html/html_tables.asp and extract all rows from the table with company names and countries.

🚀 Setup Instructions
1. Clone this repository
bash
Copy
Edit
git clone https://github.com/svharivinod/mcpdemo.git
cd mcpdemo
2. Install Python dependencies
Make sure you're using Python 3.11+ (as required by mcp-use).

bash
Copy
Edit
python -m venv .venv
.venv\Scripts\activate  # On Windows
# source .venv/bin/activate  # On Mac/Linux

uv pip install -r requirements.txt  # If using uv
3. Install Node + Playwright
If not already installed:

bash
Copy
Edit
npm install
npx playwright install
4. Set up your .env file
Create a .env file with your OpenAI API key:

ini
Copy
Edit
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
✅ Do not commit this file (it’s ignored via .gitignore).

5. Run the chatbot
bash
Copy
Edit
uv run app.py
🔍 Example Prompts You Can Try
Search g-search for "best generative AI apps in 2025"

Use Playwright to visit https://example.com and extract the heading

Type 'exit' to quit or 'clear' to reset memory

📁 Project Structure
bash
Copy
Edit
.
├── app.py                    # Main chatbot loop
├── browser_mcp.json          # MCP tool configuration
├── tools/
│   └── google-search/        # Custom Google scraper using Playwright
│       └── server.js
├── requirements.txt
├── package.json              # Node.js dependencies (Playwright)
└── .env                      # Your OpenAI API key (not tracked)
📌 Notes
You must have a valid OpenAI API key to use this chatbot.

.env is excluded from Git to protect your secrets.

Supports custom tools defined via MCP and Playwright integrations.
