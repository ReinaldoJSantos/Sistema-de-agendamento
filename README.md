# Sistema de Agendamento — FastAPI

Como executar localmente:

1. Criar e ativar um ambiente virtual (Linux/macOS):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Instalar dependências:

```bash
pip install -r requirements.txt
```

3. Rodar o servidor em modo de desenvolvimento:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

4. Testar o endpoint:

Abra `http://localhost:8000/` no navegador ou use `curl`.

Executar testes:

```bash
pytest -q
```
