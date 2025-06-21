# Automated Book Publication Workflow

This project demonstrates a full workflow automation pipeline for AI-powered book chapter processing and publishing. It includes web scraping, AI rewriting, human-in-the-loop review, and version-controlled storage using ChromaDB.

## Overview

The workflow is designed to automate the following:

1. **Scraping & Screenshots**: Extracts content and captures screenshots from target URLs using Playwright and FastAPI.
2. **AI Writing & Review**: Uses LLMs (e.g., Gemini or OpenAI) to rewrite chapters while preserving original story elements.
3. **Human-in-the-Loop**: Sends rewritten content to human reviewers via email or Notion, enabling editing and approval before finalization.
4. **Agentic API**: Integrates AI agents using n8n to manage prompt flow, revisions, and content decisions.
5. **ChromaDB Storage**: Final content is stored in ChromaDB for versioning and intelligent RL-based search.
6. **RL Search Workflow**: Implements retrieval of stored chapters based on vector similarity, enabling reinforcement-style interactions.

---

## Technologies Used

- **Python** (FastAPI, Playwright, BeautifulSoup)
- **n8n** (for orchestrating the workflow)
- **ChromaDB** (for vector storage and semantic search)
- **Notion API** (for human review and editing)
- **Docker** (for isolated deployment)
- **LLMs** (Gemini or OpenAI for AI Agents)
- **SQLite** (optional default database for n8n)


## Folder Structure

- `code/` – Contains Python backend (`main.py`, `scrape_script.py`, `requirements.txt`, etc.)
- `workflows/` – Contains exported `.json` of the n8n workflow and screenshots of nodes.
- `video/` – Contains the recorded walkthrough or demo video.
- `.gitignore` – Prevents unnecessary files from being tracked.



## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/automated-book-publication.git
cd automated-book-publication

