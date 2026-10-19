# Úloha: Hierarchie úložišť čísel (Storage, Stack, Queue)

Jednoduchá výuková úloha pro žáky zaměřená na objektově orientované programování (dědičnost, polymorfismus, zapouzdření) a základní datové struktury: **Zásobník (Stack / LIFO)** a **Fronta (Queue / FIFO)**.

---

## Dokumentace a výukové materiály

Podrobné výukové materiály a průvodci se nachází ve složce `docs/`:

* **[docs/DATOVE_STRUKTURY.md](docs/DATOVE_STRUKTURY.md)** – Podrobné vysvětlení principu Storage, Stack (LIFO) a Queue (FIFO), diagram tříd a OOP principy.
* **[docs/UNIT_TESTING.md](docs/UNIT_TESTING.md)** – Průvodce unit testováním v Pythonu (`unittest`) pro žáky.
* **[docs/DOCKER_VYSVETLENI.md](docs/DOCKER_VYSVETLENI.md)** – Polopatické vysvětlení Dockeru a Docker Compose.

---

## Struktura projektu

```text
.
├── src/                      # Zdrojové kódy aplikace
│   ├── __init__.py
│   └── storage.py            # Třídy Storage, Stack a Queue
├── tests/                    # Automatické unit testy
│   ├── __init__.py
│   └── test_storage.py       # Testovací sada pro ověření funkčnosti
├── docs/                     # Průvodci a dokumentace
│   ├── DATOVE_STRUKTURY.md   # Vysvětlení Storage, Stack a Queue
│   ├── DOCKER_VYSVETLENI.md  # Polopatické vysvětlení Dockeru
│   └── UNIT_TESTING.md       # Výukový průvodce testováním pro žáky
├── Dockerfile                # Definice Docker kontejneru pro spuštění testů
├── docker-compose.yml        # Pohodlné spuštění s live napojením svazku
├── .dockerignore             # Ignorování dočasných souborů při buildu
└── README.md
```

---

## Jak spustit testy

### 1. Lokálně (bez Dockeru)

Požadavek: Nainstalovaný Python 3.8+

```bash
# Automatické vyhledání a spuštění všech testů ve složce tests:
python -m unittest discover -s tests -v
```

Nebo lze spustit přímo soubor s testy:
```bash
python tests/test_storage.py -v
```

### 2. Pomocí Dockeru

#### Sestavení a spuštění kontejneru:
```bash
docker build -t storage-lifo-fifo-test .
docker run --rm --name storage-lifo-fifo-test storage-lifo-fifo-test
```

#### Nebo pomocí Docker Compose (doporučeno pro žáky):
Díky napojenému svazku (volume) mohou žáci upravovat kód v `src/storage.py` a změny se okamžitě projeví bez nutnosti znovu volat `docker build`:
```bash
docker compose up --build
```
Pro další spuštění po úpravě kódu stačí:
```bash
docker compose up
```
