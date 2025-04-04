# 🏛️ Municipality Lookup

**Municipality Lookup** is a lightweight Python library for retrieving information about Italian municipalities, including province, land registry office, national and cadastral codes.

It supports exact and fuzzy search (useful in OCR or typo-prone contexts) and is designed to be fast, cache-friendly and developer-friendly.

---

## 📦 Installation

Install via pip:

```bash
pip install municipality-lookup
```

---

## 🚀 Basic usage

```python
from municipality_lookup.instance import get_db

db = get_db()

# Exact search
print(db.get_by_name("ABANO TERME"))

# Fuzzy search (handles typos or partial names)
print(db.get_by_name("abno term"))

# Get all provinces
print(db.get_all_provinces())

# Get all land registries
print(db.get_all_land_registries())
```

---

## 📄 Data source

The dataset used in this library is based on publicly available information provided by:

🔗 [https://www.visurasi.it/elenco-conservatorie-e-comuni](https://www.visurasi.it/elenco-conservatorie-e-comuni)

The data is stored in CSV format and can be easily updated.

---

## 🧪 Running tests

After cloning the repo, run:

```bash
pytest
```

---

## 📁 Expected CSV format

The file must contain the following headers:

```
Comune,Provincia,Conservatoria di Competenza,Codice Nazionale,Codice Catastale
```

Each row should represent a municipality and its associated metadata.

---

## 📜 License

MIT © Andrea Iannazzo