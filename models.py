from pydantic import BaseModel
from datetime import datetime
from typing import Optional
    
class ArticleURL(BaseModel):
    url: str

class NewsArticle(BaseModel):
    title: str
    url: str
    source: str
    published_at: datetime
    summary: Optional[str] = None
    author: Optional[str] = None
    description: str
    image: Optional[str] = None
    category: Optional[str] = None
    language: Optional[str] = None
    country: Optional[str] = None
