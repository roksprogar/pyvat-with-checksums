import pytest
from pyvat_with_checksums.core import check_vat

VALID_VATS = [
    "SK1025529197",
    "SK2020032377",
    "SK2020073528",
    "SK2020077345",
    "SK2020255787",
    "SK2020261353",
    "SK2020264939",
    "SK2020273893",
    "SK2020278766",
    "SK2020317244",
    "SK2020325109",
    "SK2020325516",
    "SK2020329278",
    "SK2020350332",
    "SK2020351993",
    "SK2020358263",
    "SK2020431710",
    "SK2020527300",
    "SK2020798637",
    "SK2020845255",
    "SK2020845332",
    "SK2021116889",
    "SK2021252827",
    "SK2021776207",
    "SK2021783357",
    "SK2021853504",
    "SK2021885888",
    "SK2021900804",
    "SK2021905776",
    "SK2021947180",
    "SK2022199432",
    "SK2022229374",
    "SK2022441168",
    "SK2022569791",
    "SK2022579152",
    "SK2022832394",
    "SK2023150701",
    "SK2023369381",
    "SK2023386805",
    "SK2022742458",
    "SK7020000119",
    "SK7020000207",
    "SK7020000317",
    "SK7020000427",
    "SK7020000680",
]

INVALID_VATS = ["SK5407062531", "SK7020001680"]


@pytest.mark.parametrize("vat", VALID_VATS)
def test_slovakia__republic_valid(vat):
    result = check_vat(vat)
    assert result.is_valid, f"Expected {vat} to be valid for Slovakia Republic"
    assert result.country.name == "Slovakia Republic"


@pytest.mark.parametrize("vat", INVALID_VATS)
def test_slovakia__republic_invalid(vat):
    result = check_vat(vat)
    # Some invalid VATs might match the format but fail the check digit,
    # or fail the format entirely.
    # But result.is_valid should definitely be False.
    assert not result.is_valid, f"Expected {vat} to be invalid for Slovakia Republic"
