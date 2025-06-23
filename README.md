# Automated Book Publication Workflow

This project builds an automated workflow for fetching book chapters from the web, rewriting them using AI, and managing versions with human review and ChromaDB integration. It is built using Docker, FastAPI, Playwright, and n8n for orchestrating the workflow.

## Features

- Scraping: Fetch chapter text and screenshot using Playwright
- AI Writing: Rewrite story using an LLM (e.g., Gemini)
- Human Review: Integrate manual approval via Notion and email
- Storage: Store final version in ChromaDB
- Search: Use a keyword to retrieve the best-matching rewritten story from ChromaDB
- Version Control: RL-style feedback loop with search consistency

---

## Folder Structure

```
automated-book-workflow/
│
├── scripts/
│   ├── main.py                # FastAPI backend
│   ├── scrape_script.py       # Web scraper and screenshot logic
│   ├── requirements.txt
│   └── Dockerfile             # Dockerfile for scraper service
│
├── Dockerfile.n8n             # Custom Dockerfile for n8n patching
├── docker-compose.yml         # Launches scraper and n8n services
│
├── workflows/
│   ├── My_workflow.json       # Exported workflow from n8n
│   └── screenshots/
│       └── workflow.png       # Screenshot of the workflow
│
└── README.md                  # Project documentation
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/automated-book-workflow.git
cd automated-book-workflow
```

### 2. Run the Application

Ensure Docker is installed and running.

```bash
docker-compose up --build
```

This command will launch:

- FastAPI backend (scraper + ChromaDB interface) on port `8000`
- n8n workflow editor on port `5678`

---

## Access the Services

- **n8n Editor UI**: [http://localhost:5678](http://localhost:5678)
- **Scraping API**: `GET http://localhost:8000/scrape?url=<chapter_url>`
- **Screenshot**: `GET http://localhost:8000/screenshot`
- **ChromaDB Insertion**: `POST http://localhost:8000/add-to-chroma`
- **ChromaDB Search**: `GET http://localhost:8000/search?query=keyword`

---

## Notion & Email Integration

- Notion API is used to log rewritten content for manual human approval
- Email is sent with approval link using `Send Email` node in n8n
- Upon approval, content is POSTed to `/add-to-chroma`

---

## ChromaDB Integration

ChromaDB is used for semantic storage and retrieval of approved chapter content.

### 📦 Storage
Once a chapter is approved by a human reviewer, it is automatically stored in ChromaDB using a POST request to `/add-to-chroma`. The stored content includes:

- `title`: The chapter title
- `content`: The rewritten story (max 2000 characters)
- `notion_url`: The Notion page where the editor reviewed it
-  `screen_shot`: The Screenshot of the Website page

### 🔍 Retrieval
Search queries are sent to `/search?query=<keyword>`, which returns the most relevant chapters based on vector similarity.

### 🧾 Metadata
Each ChromaDB entry stores associated metadata:
- `title`
- `notion_url`
- `content`

This enables organized retrieval and traceability of chapter versions.

### ♻️ RL-style Feedback Loop
The workflow supports future extension into reinforcement learning-style feedback loops. Editors can give feedback on retrieved results, which can be used to refine search behavior and rewriting performance over time.


## Environment Configuration

In `docker-compose.yml`, the following variables are set:

```yaml
N8N_DATABASE_TYPE=sqlite
N8N_BASIC_AUTH_ACTIVE=true
N8N_BASIC_AUTH_USER=myth_S
N8N_BASIC_AUTH_PASSWORD=xxxxxx
```

Make sure to configure SMTP credentials in n8n if using email functionality.

---

