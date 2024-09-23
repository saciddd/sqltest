from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQL Server bağlantısı için URL (ayarlamayı yapın)
DATABASE_URL = "mssql+pyodbc://sa:20,@localhost/mercis?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Veritabanı tablolarını oluşturma
def init_db():
    Base.metadata.create_all(bind=engine)
