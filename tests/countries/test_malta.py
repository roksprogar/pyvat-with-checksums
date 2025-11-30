import pytest
from pyvat_with_checksums.core import check_vat

VALID_VATS = [
    "MT10126313",
    "MT10271622",
    "MT10365719",
    "MT10414318",
    "MT10601519",
    "MT10830531",
    "MT10988628",
    "MT11012007",
    "MT11189317",
    "MT11407334",
    "MT11539237",
    "MT11612810",
    "MT11622530",
    "MT12041610",
    "MT12135215",
    "MT12667313",
    "MT12691212",
    "MT12894031",
    "MT13271118",
    "MT14024410",
    "MT14391532",
    "MT14632420",
    "MT14675314",
    "MT15750503",
    "MT15861920",
    "MT15903903",
    "MT16364430",
    "MT16509511",
    "MT16632722",
    "MT16657432",
    "MT16735601",
    "MT16910734",
    "MT17158231",
    "MT17727224",
    "MT17869211",
    "MT18177531",
    "MT18821225",
    "MT19420526",
    "MT19677315",
    "MT19738201",
    "MT20035007",
    "MT20250021",
    "MT20390516",
    "MT20973507",
]

INVALID_VATS = ["MT2039051", "MT20390515"]


@pytest.mark.parametrize("vat", VALID_VATS)
def test_malta_valid(vat):
    result = check_vat(vat)
    assert result.is_valid, f"Expected {vat} to be valid for Malta"
    assert result.country.name == "Malta"


@pytest.mark.parametrize("vat", INVALID_VATS)
def test_malta_invalid(vat):
    result = check_vat(vat)
    # Some invalid VATs might match the format but fail the check digit,
    # or fail the format entirely.
    # But result.is_valid should definitely be False.
    assert not result.is_valid, f"Expected {vat} to be invalid for Malta"
