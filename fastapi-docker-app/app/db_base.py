from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

DATABASE_URL = "mysql+pymysql://root:password@mysql/project_db"

engine = create_engine(DATABASE_URL)
Base = declarative_base()
