import pytest
from pyvat_with_checksums.core import check_vat

VALID_VATS = ['ADF000000F', 'ADE000000E', 'ADA000000A', 'ADL000000L', 'ADE000000E', 'ADC000000C', 'ADD000000D', 'ADG000000G', 'ADO000000O', 'ADP000000P', 'ADU000000U']

INVALID_VATS = ['AD00000000', 'ADM000000M', 'ADP000000']

@pytest.mark.parametrize("vat", VALID_VATS)
def test_andorra_valid(vat):
    result = check_vat(vat)
    assert result.is_valid, f"Expected {vat} to be valid for Andorra"
    assert result.country.name == 'Andorra'

@pytest.mark.parametrize("vat", INVALID_VATS)
def test_andorra_invalid(vat):
    result = check_vat(vat)
    # Some invalid VATs might match the format but fail the check digit, 
    # or fail the format entirely. 
    # But result.is_valid should definitely be False.
    assert not result.is_valid, f"Expected {vat} to be invalid for Andorra"
