import pytest
from pyvat_with_checksums.core import check_vat

VALID_VATS = ['LU00000000', 'LU10000356', 'LU00000202', 'LU00000303', 'LU00000404', 'LU00002020', 'LU00000606', 'LU00000707', 'LU00000808', 'LU00001010', 'LU00001111', 'LU00001212', 'LU00001414', 'LU00001515', 'LU00001616', 'LU00001818', 'LU00001919', 'LU00002020', 'LU10294056', 'LU11082217', 'LU11238870', 'LU11787741', 'LU15027442', 'LU15477706', 'LU16018776', 'LU16999000', 'LU17389679', 'LU17439746', 'LU17466042', 'LU17596310', 'LU18743400', 'LU18878516', 'LU19009176', 'LU19209331', 'LU20165772', 'LU20260743', 'LU20417913', 'LU21114032', 'LU22326250', 'LU22944200', 'LU23238809', 'LU23537155', 'LU24184936', 'LU24496840', 'LU25318872']

INVALID_VATS = ['LU10000350', 'LU00000200', 'LU00000300', 'LU00000400', 'LU00002021', 'LU00000600', 'LU00000700', 'LU00000800']

@pytest.mark.parametrize("vat", VALID_VATS)
def test_luxembourg_valid(vat):
    result = check_vat(vat)
    assert result.is_valid, f"Expected {vat} to be valid for Luxembourg"
    assert result.country.name == 'Luxembourg'

@pytest.mark.parametrize("vat", INVALID_VATS)
def test_luxembourg_invalid(vat):
    result = check_vat(vat)
    # Some invalid VATs might match the format but fail the check digit, 
    # or fail the format entirely. 
    # But result.is_valid should definitely be False.
    assert not result.is_valid, f"Expected {vat} to be invalid for Luxembourg"
