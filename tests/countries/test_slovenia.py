import pytest
from pyvat_with_checksums.core import check_vat

VALID_VATS = [
    "SI10693661",
    "SI10830316",
    "SI11427205",
    "SI14246821",
    "SI14824221",
    "SI15779092",
    "SI17659957",
    "SI23512580",
    "SI23887729",
    "SI24995975",
    "SI29664373",
    "SI31162991",
    "SI37923331",
    "SI40226743",
    "SI42780071",
    "SI44156111",
    "SI45835985",
    "SI47431857",
    "SI47640308",
    "SI47992115",
    "SI49449389",
    "SI50223054",
    "SI51049406",
    "SI51387417",
    "SI52847349",
    "SI57635773",
    "SI59038551",
    "SI63580152",
    "SI64496481",
    "SI65056345",
    "SI67593321",
    "SI68297530",
    "SI73567906",
    "SI80040306",
    "SI81716338",
    "SI81931247",
    "SI82155135",
    "SI84667044",
    "SI87916452",
    "SI91132550",
    "SI92351069",
    "SI94314527",
    "SI98511734",
]

INVALID_VATS = ["SI05936241"]


@pytest.mark.parametrize("vat", VALID_VATS)
def test_slovenia_valid(vat):
    result = check_vat(vat)
    assert result.is_valid, f"Expected {vat} to be valid for Slovenia"
    assert result.country.name == "Slovenia"


@pytest.mark.parametrize("vat", INVALID_VATS)
def test_slovenia_invalid(vat):
    result = check_vat(vat)
    # Some invalid VATs might match the format but fail the check digit,
    # or fail the format entirely.
    # But result.is_valid should definitely be False.
    assert not result.is_valid, f"Expected {vat} to be invalid for Slovenia"
