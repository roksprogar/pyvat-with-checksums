import pytest
from pyvat_with_checksums.core import check_vat, VatCheckResult

def test_check_vat_invalid_country():
    result = check_vat('XX123456')
    assert not result.is_valid
    assert not result.is_supported_country
    assert result.country is None

def test_check_vat_valid_austria():
    result = check_vat('ATU12011204')
    assert result.is_valid
    assert result.is_valid_format
    assert result.is_supported_country
    assert result.country.name == 'Austria'

def test_check_vat_invalid_austria():
    result = check_vat('ATU12011205')
    assert not result.is_valid
    assert result.is_valid_format # Format matches regex
    assert result.is_supported_country
    assert result.country.name == 'Austria'
