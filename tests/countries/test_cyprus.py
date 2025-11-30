import pytest
from pyvat_with_checksums.core import check_vat

VALID_VATS = ['CY00001067Y', 'CY00376309R', 'CY00506026O', 'CY00709533C', 'CY00714754A', 'CY10000314J', 'CY10000463Y', 'CY10008146K', 'CY10018402C', 'CY10008489A', 'CY10030661B', 'CY10030954F', 'CY10111176Z', 'CY10111474A', 'CY10272781S', 'CY10283929R', 'CY10156988E', 'CY10157423I', 'CY10165829P', 'CY10166866Y', 'CY10173610U', 'CY10188550T', 'CY10221051V', 'CY10227520I', 'CY10231803U', 'CY10244276R', 'CY10247148S', 'CY10259033P', 'CY10259584H', 'CY10265331J', 'CY10269393H', 'CY10272781S', 'CY10274481T', 'CY10110278D', 'CY30009560X', 'CY90000265T', 'CY90000448S', 'CY90002066W', 'CY99000027S', 'CY99200002N']

INVALID_VATS = ['CY0', 'CY00000000W', 'CY12000000C', 'CY12000139V']

@pytest.mark.parametrize("vat", VALID_VATS)
def test_cyprus_valid(vat):
    result = check_vat(vat)
    assert result.is_valid, f"Expected {vat} to be valid for Cyprus"
    assert result.country.name == 'Cyprus'

@pytest.mark.parametrize("vat", INVALID_VATS)
def test_cyprus_invalid(vat):
    result = check_vat(vat)
    # Some invalid VATs might match the format but fail the check digit, 
    # or fail the format entirely. 
    # But result.is_valid should definitely be False.
    assert not result.is_valid, f"Expected {vat} to be invalid for Cyprus"
