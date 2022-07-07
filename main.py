from fastapi import FastAPI, Request
from scrapper.controller import scrapCreation, scrapperdetails

app = FastAPI()


@app.get("/")
async def get_data(request: Request, id: str):
    """router to get the desired data"""
    return scrapperdetails(id=id)


@app.post("/create")
async def create_data(request: Request):
    """router to post the scrapped data to database"""
    return scrapCreation()
