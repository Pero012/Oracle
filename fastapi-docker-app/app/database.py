from sqlalchemy.orm import sessionmaker
from .db_base import engine, Base

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    from .models import Base  # Ensure all models are imported
    Base.metadata.create_all(bind=engine)
