from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
   DATABASE_URL,
    pool_pre_ping=True,
    #connect_args={
     #   "ssl":{
         #   "ca": r"C:/Users/hp/Downloads/isrgrootx1.pem"
     #   }
    #}
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()  