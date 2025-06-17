# 🤖 MCPDemo — AI Chat Agent with OpenAI, Playwright & Custom Tools

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green)
![OpenAI](https://img.shields.io/badge/OpenAI-API-enabled-ff69b4)
![Playwright](https://img.shields.io/badge/Playwright-enabled-yellow)

A powerful command-line AI chatbot built using:

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

```bash
git clone https://github.com/svharivinod/mcpdemo.git
cd mcpdemo


