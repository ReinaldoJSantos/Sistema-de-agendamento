from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.routes import auth, health, users, admin
from app.core.database import engine, Base

app = FastAPI(title="Sistema de Agendamento")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(admin.router)
app.include_router(health.router)
