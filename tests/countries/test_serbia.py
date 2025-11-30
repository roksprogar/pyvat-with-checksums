import pytest
from pyvat_with_checksums.core import check_vat

VALID_VATS = [
    "RS100010812",
    "RS100182160",
    "RS100262959",
    "RS101052694",
    "RS101123484",
    "RS101511068",
    "RS101626723",
    "RS101660236",
    "RS101917688",
    "RS103257368",
    "RS102898984",
    "RS104774509",
    "RS105066236",
    "RS105101011",
    "RS105795301",
    "RS105922971",
    "RS106193133",
    "RS106414286",
    "RS106963932",
    "RS107382147",
    "RS129391320",
]

INVALID_VATS = ["RS12939132", "RS1293913201", "RS129391321"]


@pytest.mark.parametrize("vat", VALID_VATS)
def test_serbia_valid(vat):
    result = check_vat(vat)
    assert result.is_valid, f"Expected {vat} to be valid for Serbia"
    assert result.country.name == "Serbia"


@pytest.mark.parametrize("vat", INVALID_VATS)
def test_serbia_invalid(vat):
    result = check_vat(vat)
    # Some invalid VATs might match the format but fail the check digit,
    # or fail the format entirely.
    # But result.is_valid should definitely be False.
    assert not result.is_valid, f"Expected {vat} to be invalid for Serbia"
