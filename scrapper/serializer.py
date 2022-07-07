from pydantic import BaseModel


class ScrapperSerializer(BaseModel):
    data: dict = {}

