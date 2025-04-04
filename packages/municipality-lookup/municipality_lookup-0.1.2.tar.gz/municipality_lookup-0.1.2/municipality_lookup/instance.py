import importlib.resources
from municipality_lookup import MunicipalityDB

_db_instance = None

def get_db(csv_path: str = None) -> MunicipalityDB:
    global _db_instance
    if _db_instance is None:
        if csv_path is None:
            # Load built-in CSV
            with importlib.resources.path("municipality_lookup.data", "comuni.csv") as p:
                csv_path = str(p)
        _db_instance = MunicipalityDB(csv_path)
    return _db_instance
