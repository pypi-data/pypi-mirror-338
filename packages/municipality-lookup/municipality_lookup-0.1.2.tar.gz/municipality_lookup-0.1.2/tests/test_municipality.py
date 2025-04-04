from municipality_lookup.instance import get_db

def test_exact_match():
    db = get_db()
    result = db.get_by_name("ABANO TERME")
    assert result is not None
    assert result.province == "PD"

def test_fuzzy_match():
    db = get_db()
    result = db.get_by_name("abno terne", min_score=0.8)
    assert result is not None
    assert "ABANO TERME" in result.name.upper()

def test_fuzzy_match_space():
    db = get_db()
    result = db.get_by_name("A L E S S A N D R I A", min_score=0.8)
    assert result is not None
    assert "ALESSANDRIA" in result.name.upper()
