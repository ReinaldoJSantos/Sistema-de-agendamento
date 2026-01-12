from fastapi import FastAPI


app = FastAPI(title="Sistema de Agendamento")


@app.get("/health")
async def healt():
    return {"message": "ok"}
