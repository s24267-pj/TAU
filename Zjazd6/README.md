# Zjazd 6


## Wymagania
- Python 3.8+
- fastapi
- pydantic
- pytest
- httpx
- uvicorn


## Uruchamianie aplikacji

1. Startowanie FASTapi:
   ```bash
   uvicorn main:app --reload
   ```

2. Otwórz przeglądarkę i przejdź pod:
   - **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Testowanie
```bash
   pytest main.py
   ```