import pytest
from pyvat_with_checksums.core import check_vat

VALID_VATS = ['FI09853608', 'FI00000027', 'FI00000035', 'FI00000043', 'FI00000174', 'FI00000078', 'FI00000086', 'FI00000094', 'FI00000115', 'FI00000123', 'FI00000131', 'FI00000166', 'FI00000174', 'FI00000182', 'FI00000203', 'FI00000211', 'FI00000238', 'FI01244162', 'FI02459042', 'FI06312080', 'FI08405256', 'FI09441865', 'FI08326937', 'FI10154054', 'FI10227508', 'FI15380325', 'FI15501019', 'FI15482348', 'FI15719544', 'FI16802358', 'FI17377883', 'FI17405469', 'FI17764656', 'FI18261444', 'FI18919760', 'FI20303674', 'FI21044950', 'FI22780669', 'FI22811357', 'FI22283574', 'FI22969621', 'FI22975669', 'FI24498085', 'FI24710461']

INVALID_VATS = ['FI09853601', 'FI00000023', 'FI00000036', 'FI00000048', 'FI00000173', 'FI00000071']

@pytest.mark.parametrize("vat", VALID_VATS)
def test_finland_valid(vat):
    result = check_vat(vat)
    assert result.is_valid, f"Expected {vat} to be valid for Finland"
    assert result.country.name == 'Finland'

@pytest.mark.parametrize("vat", INVALID_VATS)
def test_finland_invalid(vat):
    result = check_vat(vat)
    # Some invalid VATs might match the format but fail the check digit, 
    # or fail the format entirely. 
    # But result.is_valid should definitely be False.
    assert not result.is_valid, f"Expected {vat} to be invalid for Finland"
