from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///reservas.db")
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)