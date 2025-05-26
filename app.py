from fastapi import FastAPI
from pydantic import BaseModel
from llm import LLM
from models import ArticleURL
from scraper import WebScraper
import json

app = FastAPI()

llm_instance = LLM(model_name="gemma2-9b-it")
scraper = WebScraper()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/articles")
async def get_articles():
    with open("news_data.json", "r") as f:
        data = json.load(f)
    return data

@app.post("/summarize")
async def summarize_article(article_url: ArticleURL):
    scraped_text = scraper.scrape_text(article_url.url)
    summary = llm_instance.generate(text=scraped_text)
    return {"status": "success", "content": scraped_text, "summary": summary}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)