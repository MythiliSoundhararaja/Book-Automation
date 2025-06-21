from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from pydantic import BaseModel
from scrape_script import scrape_chapter
import chromadb
import uuid

app = FastAPI()

@app.get("/scrape")
def scrape(url: str = Query(...)):
    result = scrape_chapter(url)
    return result

@app.get("/screenshot")
def get_screenshot():
    return FileResponse("chapter1.png", media_type="image/png")

client = chromadb.Client()
collection = client.get_or_create_collection("rewritten_stories")

class ChromaData(BaseModel):
    title: str
    content: str
    notion_url: str
    screenshot_path: str = ""

@app.post("/add-to-chroma")
def add_to_chroma(data: ChromaData):
    try:
        doc_id = str(uuid.uuid4())
        collection.add(
            documents=[data.content],
            metadatas=[{
                "title": data.title,
                "notion_url": data.notion_url
            }],
            ids=[doc_id]
        )
        return {"status": "success", "id": doc_id}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/search")
def search_content(query: str):
    try:
        results = collection.query(
            query_texts=[query],
            n_results=3
        )
        return {"results": results}
    except Exception as e:
        return {"error": str(e)}


