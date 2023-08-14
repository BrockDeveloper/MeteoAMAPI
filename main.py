from fastapi import FastAPI, HTTPException
from webscraper import WebScraper

app = FastAPI()


@app.get("/{location}")
def get_weather(location: str):

    try:
        scraper = WebScraper(location)
        data = scraper.get()

        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
    