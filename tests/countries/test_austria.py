import pytest
from pyvat_with_checksums.core import check_vat

VALID_VATS = [
    "ATU00000024",
    "ATU00000033",
    "ATU00000042",
    "ATU00000202",
    "ATU00000060",
    "ATU00000079",
    "ATU00000088",
    "ATU00000104",
    "ATU00000113",
    "ATU00000122",
    "ATU00000140",
    "ATU00000159",
    "ATU00000168",
    "ATU00000186",
    "ATU00000195",
    "ATU00000202",
    "ATU12011204",
    "ATU10223006",
    "ATU15110001",
    "ATU15394605",
    "ATU15416707",
    "ATU15662209",
    "ATU16370905",
    "ATU23224909",
    "ATU25775505",
    "ATU28560205",
    "ATU28609707",
    "ATU28617100",
    "ATU29288909",
    "ATU37675002",
    "ATU37785508",
    "ATU37830200",
    "ATU38420507",
    "ATU38516405",
    "ATU39364503",
    "ATU42527002",
    "ATU43666001",
    "ATU43716207",
    "ATU45766309",
    "ATU47977701",
    "ATU49487700",
    "ATU51009402",
    "ATU51507409",
    "ATU51749808",
    "ATU52699307",
    "ATU57477929",
    "ATU58044146",
    "ATU61255233",
    "ATU61993034",
    "ATU62134737",
    "ATU62593358",
    "ATU62765626",
    "ATU62895905",
    "ATU62927729",
    "ATU63436026",
    "ATU64487479",
    "ATU64762368",
    "ATU64727905",
    "ATU64938189",
    "ATU66664013",
    "ATU66889218",
]

INVALID_VATS = [
    "ATV66889218",
    "ATU10223001",
    "ATU10223002",
    "ATU10223003",
    "ATU10223004",
    "ATU10223005",
    "ATU10223007",
]


@pytest.mark.parametrize("vat", VALID_VATS)
def test_austria_valid(vat):
    result = check_vat(vat)
    assert result.is_valid, f"Expected {vat} to be valid for Austria"
    assert result.country.name == "Austria"


@pytest.mark.parametrize("vat", INVALID_VATS)
def test_austria_invalid(vat):
    result = check_vat(vat)
    # Some invalid VATs might match the format but fail the check digit,
    # or fail the format entirely.
    # But result.is_valid should definitely be False.
    assert not result.is_valid, f"Expected {vat} to be invalid for Austria"
