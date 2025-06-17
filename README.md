# 🧠 ToolSage - AI-powered assistant that uses OpenAI + Playwright to browse, extract, and automate websites

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green)
![OpenAI API](https://img.shields.io/badge/OpenAI-API--Key-blueviolet?logo=openai&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-enabled-yellow)
![LangChain](https://img.shields.io/badge/LangChain-integrated-9cf?logo=langchain&logoColor=black)
![uv](https://img.shields.io/badge/uv-python%20packager-informational?logo=python)
![GitHub Repo stars](https://img.shields.io/github/stars/svharivinod/mcpdemo?style=social)

ToolSage is an AI-powered command-line assistant that uses OpenAI's GPT-4o-mini alongside powerful browser tools like Playwright via MCP. Designed for real-time web data extraction, ToolSage can browse websites, interact with pages, and extract structured content. For example, it can:
- 🛍️ Visit [Books to Scrape](https://books.toscrape.com) and return book titles and prices
- 📝 Scrape 3 quotes and their authors from [Quotes to Scrape](https://quotes.toscrape.com)
- 📊 Extract company names and countries from HTML tables on [W3Schools](https://www.w3schools.com/html/html_tables.asp)

Whether you want to automate browsing, scrape structured content, or query the web conversationally — ToolSage does it all with natural language. A powerful command-line AI chatbot built using:

- 🧠 [OpenAI's GPT-4o-mini](https://platform.openai.com/)
- 🌐 Google Search via a custom Playwright MCP tool
- 🧰 Support for DuckDuckGo, Airbnb, and more through the MCP framework

---

## ✨ Features

- Natural multi-turn conversation with memory
- Tool-augmented queries like:
  - `"Search g-search for top AI trends in 2025"`
  - `"Use Playwright to scrape https://example.com"`
- Extendable with your own tools via `tools/`

---

## 📁 Project Structure

mcpdemo/
├── app.py # Main interactive chat logic
├── browser_mcp.json # MCP tool configuration
├── tools/
│ └── google-search/
│ └── server.js # Custom Google scraper using Playwright
├── .env # OpenAI API key (ignored)
├── .gitignore
├── requirements.txt
├── package.json # NodeJS deps for Playwright
└── README.md

---

## 🚀 Setup Instructions

### 1. Clone the repository
- git clone https://github.com/svharivinod/mcpdemo.git
- cd mcpdemo

### 2. Setup Python
- python -m venv .venv
- .venv\Scripts\activate
- pip install -r requirements.txt

### 3. Install Node + Playwright
- npm install
- npx playwright install

### 4. Create .env file with your OpenAI key
- OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXX

### 5. Examples Prompt to Try
- Use Playwright to go to https://books.toscrape.com and list the titles and prices of the first 3 books.
- Visit https://quotes.toscrape.com with Playwright and extract 3 quotes along with their authors.
- Use Playwright to visit https://www.w3schools.com/html/html_tables.asp and extract all rows from the table with company names and countries.

### 6. How to Run
- uv run app.py OR
- python app.py

### 7. Security Note
- This repo blocks .env using .gitignore
- GitHub may reject pushes if secrets are accidentally committed (see GitHub secret scanning)

### 8. License
MIT © svharivinod




