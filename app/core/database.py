import os
from urllib.parse import quote_plus
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

raw_url = os.getenv("DATABASE_URL")

# Se a URL vier completa do .env mas a senha tiver @,
# o ideal é separar as variáveis no .env:
# DB_USER=admin
# DB_PASS=senh@com@
# DB_HOST=127.0.0.1
# DB_NAME=meu_db

user = os.getenv("DB_USER")
passwd = quote_plus(os.getenv("DB_PASS", ""))
host = os.getenv("DB_HOST")
db = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql+psycopg://{user}:{passwd}@{host}/{db}"
engine = create_engine(DATABASE_URL)
