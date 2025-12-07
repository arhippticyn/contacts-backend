from sqlalchemy import String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(engine)

class Contact(Base):
    __tablename__ = 'contacts'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    tel: Mapped[str] = mapped_column(String(30))

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()

Base.metadata.create_all(bind=engine)