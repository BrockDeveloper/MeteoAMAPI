from fastapi import FastAPI, HTTPException, Response
from webscraper import WebScraper
import xmltodict

app = FastAPI()


@app.get("/{location}")
def get_weather(location: str, xml: bool = False):

    try:
        scraper = WebScraper(location)
        data = scraper.get()

        if xml:
            data = data.dict()
            # define "root" element
            dict_to_xml = {"root": data}
            # convert dict to xml
            xml = xmltodict.unparse(dict_to_xml, pretty=True)
            # return xml
            return Response(content=xml, media_type="application/xml")
        else:
            return data
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
   


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(host="localhost", port=8000, reload=True, app="main:app")
    