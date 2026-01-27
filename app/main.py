from fastapi import FastAPI
from app.api.routes import auth, users, admin
from app.core.seed import create_admin_user
from app.core.database import SessionLocal, engine, Base

app = FastAPI(title="Sistema de Agendamento")

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(admin.router)


@app.on_event("startup")
def on_startup():
    # Cria as tabelas
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    create_admin_user(db)
    db.close()
