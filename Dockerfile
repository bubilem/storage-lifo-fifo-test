# Použijeme lehký oficiální Python obraz
FROM python:3.12-slim

# Nastavení pracovního adresáře v kontejneru
WORKDIR /app

# Vypnutí ukládání bytecode (.pyc) a zapnutí nebufferovaného výstupu
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# Zkopírování zdrojových kódů a testů
COPY src/ ./src/
COPY tests/ ./tests/

# Výchozí příkaz: automatické spuštění testů ze složky tests s podrobným výpisem (-v)
CMD ["python", "-m", "unittest", "discover", "-s", "tests", "-v"]
