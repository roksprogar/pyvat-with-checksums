
from pyvat_with_checksums import check_vat, VatCheckResult

def test_public_api_check_vat():
    # Test the public API exposed in __init__.py
    result = check_vat('ATU12011204')
    assert isinstance(result, VatCheckResult)
    assert result.is_valid
    assert result.country.name == 'Austria'

def test_public_api_check_vat_invalid():
    result = check_vat('INVALID')
    assert not result.is_valid
    assert not result.is_supported_country
    assert result.country is None

def test_public_api_check_vat_multi_country_resolution():
    # Test that the ambiguity resolution works via public API
    # Brazil VAT that starts with 020 (Andorra code)
    vat = '02.061.065/0001-72'
    result = check_vat(vat)
    assert result.is_valid
    assert result.country.name == 'Brazil'
