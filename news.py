import requests
import os

class NewsApi:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get('MEDIASTACK_API_KEY')
        if not self.api_key:
            raise ValueError("API key for mediastack not provided or found in environment variables.")
        self.base_url = "http://api.mediastack.com/v1/"

    def get_news(self, keywords, sources=None, categories=None, countries=None, languages=None, limit=25, offset=0, sort="published_desc"):
        params = {
            "access_key": self.api_key,
            "keywords": keywords,
            "limit": limit,
            "offset": offset,
            "sort": sort,
        }
        if sources:
            params["sources"] = sources
        if categories:
            params["categories"] = categories
        if countries:
            params["countries"] = countries
        if languages:
            params["languages"] = languages

        response = requests.get(f"{self.base_url}news", params=params)
        response.raise_for_status()
        return response.json()


if __name__ == "__main__":
    import json
    
    news_api = NewsApi()

    news_data = news_api.get_news(keywords="technology")

    with open("news_data.json", "w") as f:
        json.dump(news_data, f, indent=4)

    print("News data saved to news_data.json")
