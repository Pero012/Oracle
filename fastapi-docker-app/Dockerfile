# Koristi Python 3.9 kao osnovnu sliku
FROM python:3.9-slim

# Postavlja radni direktorij unutar kontejnera
WORKDIR /app

# Kopira datoteku sa zahtjevima
COPY requirements.txt .

# Instalira Python pakete
RUN pip install --no-cache-dir -r requirements.txt

# Kopira cijelu aplikaciju
COPY . .

# Izlaže port 8000
EXPOSE 8000

# Pokreće aplikaciju
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
