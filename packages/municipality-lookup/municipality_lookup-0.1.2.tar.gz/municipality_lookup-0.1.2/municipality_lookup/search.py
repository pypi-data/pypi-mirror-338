from difflib import SequenceMatcher
from typing import Optional
from municipality_lookup.models import Municipality

class MunicipalitySearcher:
    def __init__(self, municipalities: list[Municipality]):
        self._municipalities = municipalities
        self._index = {m.name.lower(): m for m in municipalities}

    def find_exact(self, name: str) -> Optional[Municipality]:
        return self._index.get(name.strip().lower())

    def find_similar(self, name: str, min_score: float = 0.8) -> Optional[Municipality]:
        name = name.strip().lower()
        best_match = None
        best_score = 0

        for m in self._municipalities:
            score = SequenceMatcher(None, name, m.name.lower()).ratio()
            if score > best_score and score >= min_score:
                best_match = m
                best_score = score
        return best_match
