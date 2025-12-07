from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from db import get_db, Contact
from sqlalchemy.orm import Session
from models import ContactsCreate, ContactsResponse


app = FastAPI()

origins = [
    'http://localhost:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

@app.post('/add')
def create_contact(user: ContactsCreate, db: Session = Depends(get_db)):
    # db_contact = ContactsResponse(user.name, user.Number_tel)
    new_contact = Contact(**user.model_dump())
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact

@app.get('/contacts', response_model=list[ContactsResponse])
def get_contacts(db: Session = Depends(get_db)):
    return db.query(Contact).all()

@app.delete('/delete/{contact_id}')
def delete_contacts(contact_id: int, db: Session = Depends(get_db)):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    
    db.delete(contact)
    db.commit()
    
    return contact_id