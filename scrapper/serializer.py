from pydantic import BaseModel


class ScrapperSerializer(BaseModel):
    registration_id: str
    Name: str = None
    Address: str = None
    Correspondence_Address: str = None
    Validity: str = None

