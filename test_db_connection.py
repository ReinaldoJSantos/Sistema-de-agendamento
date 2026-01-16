from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg://agendamento_user:110278cm@@127.0.0.1:5432/agendamento_db"
)

with engine.connect() as conn:
    print(conn.execute(text("SELECT 1")).scalar())
