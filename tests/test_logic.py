import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from logic.kb import urgency, is_eligible

def test_urgency_thresholds():
    assert urgency({"hours_to_expiry": 1}) == "CRITICAL"
    assert urgency({"hours_to_expiry": 3}) == "HIGH"
    assert urgency({"hours_to_expiry": 8}) == "NORMAL"

def test_dairy_requires_cold_storage():
    dairy = {"food_type":"dairy"}
    no_cold = {"needs":["dairy"], "cold_storage":False}
    cold = {"needs":["dairy"], "cold_storage":True}
    assert not is_eligible(dairy, no_cold)
    assert is_eligible(dairy, cold)
