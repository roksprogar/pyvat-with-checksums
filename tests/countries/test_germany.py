import pytest
from pyvat_with_checksums.core import check_vat

VALID_VATS = [
    "DE111111125",
    "DE113298780",
    "DE113891176",
    "DE114189102",
    "DE119429301",
    "DE122119035",
    "DE126639095",
    "DE126823642",
    "DE128575725",
    "DE128936602",
    "DE129516430",
    "DE130502536",
    "DE132507686",
    "DE136695976",
    "DE138263821",
    "DE138497248",
    "DE142930777",
    "DE145141525",
    "DE145146812",
    "DE146624530",
    "DE160459932",
    "DE184543132",
    "DE199085992",
    "DE126563585",
    "DE203159652",
    "DE220709071",
    "DE247139684",
    "DE252429421",
    "DE256319655",
    "DE262044136",
    "DE282741168",
    "DE811209378",
    "DE811363057",
    "DE812321109",
    "DE812529243",
    "DE813030375",
    "DE813189177",
    "DE813232162",
    "DE813261484",
    "DE813495425",
]

INVALID_VATS = [
    "DE111111126",
    "DE111111127",
    "DE111111128",
    "DE111111129",
    "DE111111120",
    "DE111111121",
    "DE000000020",
    "DE000000038",
    "DE000000046",
    "DE000000206",
    "DE000000062",
    "DE000000079",
    "DE000000087",
    "DE000000100",
    "DE000000118",
    "DE000000126",
    "DE000000142",
    "DE000000159",
    "DE000000167",
    "DE000000183",
    "DE000000191",
    "DE000000206",
]


@pytest.mark.parametrize("vat", VALID_VATS)
def test_germany_valid(vat):
    result = check_vat(vat)
    assert result.is_valid, f"Expected {vat} to be valid for Germany"
    assert result.country.name == "Germany"


@pytest.mark.parametrize("vat", INVALID_VATS)
def test_germany_invalid(vat):
    result = check_vat(vat)
    # Some invalid VATs might match the format but fail the check digit,
    # or fail the format entirely.
    # But result.is_valid should definitely be False.
    assert not result.is_valid, f"Expected {vat} to be invalid for Germany"
