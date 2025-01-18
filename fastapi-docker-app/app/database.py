import time
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker
from app.models import Base

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:password@mysql/project_db"

# Retry the connection
connected = False
for attempt in range(10):
    try:
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        Base.metadata.create_all(bind=engine)  # Ensure tables are created
        connected = True
        break
    except OperationalError as e:
        print(f"Database not ready, retrying in 5 seconds... (Attempt {attempt + 1}/10)")
        time.sleep(5)

if not connected:
    raise Exception("Failed to connect to the database after 10 attempts")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)