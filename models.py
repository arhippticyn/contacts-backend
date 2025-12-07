from pydantic import BaseModel, Field, field_validator

class ContactsCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=100, description="Your name")
    tel: str = Field(..., min_length=1, max_length=12, description="Number tel")
    
class ContactsResponse(ContactsCreate):
    id: int
    
    class Config:
        orm_mode = True
    