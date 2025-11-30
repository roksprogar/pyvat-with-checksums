import pytest
from pyvat_with_checksums.core import check_vat

VALID_VATS = ['LV07091910933', 'LV40003009497', 'LV40003032949', 'LV40003048583', 'LV40003125825', 'LV40003130421', 'LV40003139967', 'LV40003224680', 'LV40003254505', 'LV40003275598', 'LV40003280118', 'LV40003282138', 'LV40003287135', 'LV40003348054', 'LV40003435328', 'LV40003439368', 'LV40003453643', 'LV40003511655', 'LV40003553786', 'LV40003568404', 'LV40003576416', 'LV40003585673', 'LV40003609083', 'LV40003651875', 'LV40003702071', 'LV40003732964', 'LV40003734170', 'LV40003857687', 'LV40003921905', 'LV40008000225', 'LV40008197548', 'LV40103058465', 'LV40103189574', 'LV40103247567', 'LV40103388513', 'LV40103446084', 'LV40103592648', 'LV40103619251', 'LV41202010448', 'LV41031037436', 'LV41503031291', 'LV50003017621', 'LV50003913651', 'LV50008111541', 'LV90000022399', 'LV90000136794', 'LV90002573483']

INVALID_VATS = ['LV90001234567', 'LV12345234567', 'LV123452345672', 'LV0123']

@pytest.mark.parametrize("vat", VALID_VATS)
def test_latvia_valid(vat):
    result = check_vat(vat)
    assert result.is_valid, f"Expected {vat} to be valid for Latvia"
    assert result.country.name == 'Latvia'

@pytest.mark.parametrize("vat", INVALID_VATS)
def test_latvia_invalid(vat):
    result = check_vat(vat)
    # Some invalid VATs might match the format but fail the check digit, 
    # or fail the format entirely. 
    # But result.is_valid should definitely be False.
    assert not result.is_valid, f"Expected {vat} to be invalid for Latvia"
