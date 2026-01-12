from sqlalchemy import create_engine, text

DATABASE_URL = (
    "postgresql+psycopg://agendamento_user:110278cm@@127.0.0.1:5432/agendamento_db"
)

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    print(conn.execute(text("SELECT 1")).scalar())
