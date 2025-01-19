from sqlalchemy import Column, Integer, String
from .db_base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)  # Specify length for MySQL
    email = Column(String(255), unique=True, index=True)  # Specify length for MySQL
