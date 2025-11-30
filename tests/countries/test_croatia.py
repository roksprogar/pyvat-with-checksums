import pytest
from pyvat_with_checksums.core import check_vat

VALID_VATS = [
    "HR02574432339",
    "HR06282943396",
    "HR06631807697",
    "HR08308894711",
    "HR09993794428",
    "HR12385860076",
    "HR14553560010",
    "HR16364086764",
    "HR16491034355",
    "HR17099025134",
    "HR20649144807",
    "HR20963249418",
    "HR21213412417",
    "HR22910368449",
    "HR23448731483",
    "HR24595836665",
    "HR24897777109",
    "HR25107893471",
    "HR28639480902",
    "HR28922587775",
    "HR33392005961",
    "HR39672837472",
    "HR45726041402",
    "HR46144176176",
    "HR51200725053",
    "HR61867710134",
    "HR64871724841",
    "HR69715301002",
    "HR71434725544",
    "HR81592331325",
    "HR81889785066",
    "HR82067332481",
    "HR82659251081",
    "HR85760419184",
    "HR88776522763",
    "HR89018712265",
    "HR89789819324",
    "HR91025164621",
    "HR92889721810",
    "HR93634429487",
    "HR95976200516",
    "HR96151551854",
    "HR97405527203",
]

INVALID_VATS = ["HR9363442948", "HR93634429488", "HR936344294871"]


@pytest.mark.parametrize("vat", VALID_VATS)
def test_croatia_valid(vat):
    result = check_vat(vat)
    assert result.is_valid, f"Expected {vat} to be valid for Croatia"
    assert result.country.name == "Croatia"


@pytest.mark.parametrize("vat", INVALID_VATS)
def test_croatia_invalid(vat):
    result = check_vat(vat)
    # Some invalid VATs might match the format but fail the check digit,
    # or fail the format entirely.
    # But result.is_valid should definitely be False.
    assert not result.is_valid, f"Expected {vat} to be invalid for Croatia"
