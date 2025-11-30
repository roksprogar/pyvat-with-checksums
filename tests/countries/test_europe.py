import pytest
from pyvat_with_checksums.core import check_vat

VALID_VATS = ["EU372000052", "EU826001142"]

INVALID_VATS = ["EU123456", "EU1234567", "EU826001142123", "EU0123"]


@pytest.mark.parametrize("vat", VALID_VATS)
def test_europe_valid(vat):
    result = check_vat(vat)
    assert result.is_valid, f"Expected {vat} to be valid for Europe"
    assert result.country.name == "Europe"


@pytest.mark.parametrize("vat", INVALID_VATS)
def test_europe_invalid(vat):
    result = check_vat(vat)
    # Some invalid VATs might match the format but fail the check digit,
    # or fail the format entirely.
    # But result.is_valid should definitely be False.
    assert not result.is_valid, f"Expected {vat} to be invalid for Europe"
