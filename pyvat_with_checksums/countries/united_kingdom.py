import re
from ..core import Country


def _is_government_department(vat: str) -> bool:
    expect = 500
    return int(vat[2:5]) < expect


def _is_health_authorities(vat: str) -> bool:
    expect = 499
    return int(vat[2:5]) > expect


def _is_standard_or_commercial_number(vat: str, multipliers: list) -> bool:
    if int(vat) == 0:
        return False

    no = int(vat[:7])

    total = 0
    for i in range(7):
        total += int(vat[i]) * multipliers[i]

    check_digit = total
    while check_digit > 0:
        check_digit -= 97

    check_digit = abs(check_digit)

    if (
        check_digit == int(vat[7:9])
        and no < 9990001
        and (no < 100000 or no > 999999)
        and (no < 9490001 or no > 9700000)
    ):
        return True

    if check_digit >= 55:
        check_digit -= 55
    else:
        check_digit += 42

    expect = int(vat[7:9])
    return check_digit == expect and no > 1000000


def calc_united_kingdom(vat: str) -> bool:
    if vat.startswith("GD"):
        return _is_government_department(vat)

    if vat.startswith("HA"):
        return _is_health_authorities(vat)

    return _is_standard_or_commercial_number(
        vat, united_kingdom.rules["multipliers"]["common"]
    )


united_kingdom = Country(
    name="United Kingdom",
    codes=["GB", "GBR", "826"],
    calc_fn=calc_united_kingdom,
    rules={
        "multipliers": {"common": [8, 7, 6, 5, 4, 3, 2]},
        "regex": [
            re.compile(r"^(GB)?(\d{9})$"),
            re.compile(r"^(GB)?(\d{12})$"),
            re.compile(r"^(GB)?(GD\d{3})$"),
            re.compile(r"^(GB)?(HA\d{3})$"),
        ],
    },
)
