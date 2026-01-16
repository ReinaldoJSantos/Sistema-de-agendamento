from fastapi import FastAPI
from app.api.routes import auth, users, admin

app = FastAPI(title="Sistema de Agendamento")

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(admin.router)


@app.get("/health")
def health():
    return {"status": "ok"}
