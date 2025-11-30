import pytest
from pyvat_with_checksums.core import check_vat

VALID_VATS = [
    "CHE100416306MWST",
    "CHE101090265MWST",
    "CHE101698805MWST",
    "CHE101770851MWST",
    "CHE102534916MWST",
    "CHE102628670MWST",
    "CHE102646900MWST",
    "CHE102805222MWST",
    "CHE103051537MWST",
    "CHE104309655MWST",
    "CHE104528536MWST",
    "CHE104827884MWST",
    "CHE105121077MWST",
    "CHE105124868MWST",
    "CHE105381951MWST",
    "CHE107737562MWST",
    "CHE105789849MWST",
    "CHE105835768MWST",
    "CHE105873496MWST",
    "CHE105898444MWST",
    "CHE106480461MWST",
    "CHE106847076MWST",
    "CHE107811419MWST",
    "CHE107984669MWST",
    "CHE108017588MWST",
    "CHE108019245MWST",
    "CHE108020917MWST",
    "CHE108458018MWST",
    "CHE108672988MWST",
    "CHE109852725MWST",
    "CHE109877518MWST",
    "CHE110171891MWST",
    "CHE110257191MWST",
    "CHE112142015MWST",
    "CHE112256297MWST",
    "CHE112487804MWST",
    "CHE112591732MWST",
    "CHE113816425MWST",
    "CHE114498799MWST",
    "CHE114546487MWST",
    "CHE114932413MWST",
    "CHE115197811MWST",
    "CHE115288187MWST",
    "CHE115772649MWST",
    "CHE116032762MWST",
    "CHE116199020MWST",
    "CHE116238111MWST",
    "CHE116268856MWST",
    "CHE116272898MWST",
    "CHE116276850MWST",
    "CHE116284625MWST",
    "CHE116303292MWST",
    "CHE116303553MWST",
    "CHE116304475MWST",
    "CHE116320362MWST",
    "CHE158229508MWST",
    "CHE184633358MWST",
    "CHE255263366MWST",
    "CHE284156502MWST",
    "CHE350423893MWST",
    "CHE381569736MWST",
    "CHE408983125MWST",
    "CHE424414541MWST",
    "CHE432495116MWST",
    "CHE432825998MWST",
    "CHE432825998TVA",
    "CHE432825998IVA",
    "CHE-432.825.998 MWST",
    "CHE-432.825.998 TVA",
    "CHE-432.825.998 IVA",
]

INVALID_VATS = ["CHE-432.825.99-MWST", "CHE-432.825.9980-MWST", "CH-432.825.999-MWST"]


@pytest.mark.parametrize("vat", VALID_VATS)
def test_switzerland_valid(vat):
    result = check_vat(vat)
    assert result.is_valid, f"Expected {vat} to be valid for Switzerland"
    assert result.country.name == "Switzerland"


@pytest.mark.parametrize("vat", INVALID_VATS)
def test_switzerland_invalid(vat):
    result = check_vat(vat)
    # Some invalid VATs might match the format but fail the check digit,
    # or fail the format entirely.
    # But result.is_valid should definitely be False.
    assert not result.is_valid, f"Expected {vat} to be invalid for Switzerland"
