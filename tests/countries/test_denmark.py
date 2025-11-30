import pytest
from pyvat_with_checksums.core import check_vat

VALID_VATS = [
    "DK10000009",
    "DK10000017",
    "DK10000025",
    "DK10000157",
    "DK10000033",
    "DK10000041",
    "DK10000068",
    "DK10000076",
    "DK10000084",
    "DK10000092",
    "DK10000106",
    "DK10000114",
    "DK10000122",
    "DK10000130",
    "DK10000149",
    "DK10000157",
    "DK12935110",
    "DK18424649",
    "DK18630036",
    "DK19475298",
    "DK20214414",
    "DK20342781",
    "DK21659509",
    "DK25160924",
    "DK25760352",
    "DK25763858",
    "DK26134439",
    "DK27509185",
    "DK27919502",
    "DK28323271",
    "DK28702612",
    "DK29189757",
    "DK29206600",
    "DK29283958",
    "DK30559150",
    "DK31119103",
    "DK32569943",
    "DK32780806",
    "DK33266022",
    "DK37131415",
    "DK44023911",
    "DK67758919",
    "DK71186911",
    "DK75142412",
    "DK78805218",
]

INVALID_VATS = ["DK10000000", "DK10000010", "DK10000020", "DK10000150", "DK10000030"]


@pytest.mark.parametrize("vat", VALID_VATS)
def test_denmark_valid(vat):
    result = check_vat(vat)
    assert result.is_valid, f"Expected {vat} to be valid for Denmark"
    assert result.country.name == "Denmark"


@pytest.mark.parametrize("vat", INVALID_VATS)
def test_denmark_invalid(vat):
    result = check_vat(vat)
    # Some invalid VATs might match the format but fail the check digit,
    # or fail the format entirely.
    # But result.is_valid should definitely be False.
    assert not result.is_valid, f"Expected {vat} to be invalid for Denmark"
