import re
from typing import List
from ..core import Country


def _increase(value: int, vat: str, start: int, end: int, incr: int) -> int:
    result = value
    for i in range(start, end):
        result += int(vat[i]) * (i + incr)
    return result


def _increase2(
    value: int, vat: str, start: int, end: int, multipliers: List[int]
) -> int:
    result = value
    for i in range(start, end):
        result += int(vat[i]) * multipliers[i]
    return result


def _check_nine_length_vat(vat: str) -> bool:
    temp = _increase(0, vat, 0, 8, 1)
    expect = int(vat[8])

    total = temp % 11
    if total != 10:
        return total == expect

    temp = _increase(0, vat, 0, 8, 3)
    total = temp % 11
    if total == 10:
        total = 0

    return total == expect


def _is_physical_person(vat: str, physical_multipliers: List[int]) -> bool:
    if re.match(r"^\d\d[0-5]\d[0-3]\d\d{4}$", vat):
        month = int(vat[2:4])
        if (0 < month < 13) or (20 < month < 33) or (40 < month < 53):
            total = _increase2(0, vat, 0, 9, physical_multipliers)
            total = total % 11
            if total == 10:
                total = 0
            if total == int(vat[9]):
                return True
    return False


def _is_foreigner(vat: str, foreigner_multipliers: List[int]) -> bool:
    total = _increase2(0, vat, 0, 9, foreigner_multipliers)
    return (total % 10) == int(vat[9])


def _miscellaneous_vat(vat: str, miscellaneous_multipliers: List[int]) -> bool:
    total = _increase2(0, vat, 0, 9, miscellaneous_multipliers)
    total = 11 - (total % 11)
    if total == 10:
        return False
    if total == 11:
        total = 0
    return total == int(vat[9])


def calc_bulgaria(vat: str) -> bool:
    if len(vat) == 9:
        return _check_nine_length_vat(vat)

    multipliers = bulgaria.rules["multipliers"]
    return (
        _is_physical_person(vat, multipliers["physical"])
        or _is_foreigner(vat, multipliers["foreigner"])
        or _miscellaneous_vat(vat, multipliers["miscellaneous"])
    )


bulgaria = Country(
    name="Bulgaria",
    codes=["BG", "BGR", "100"],
    calc_fn=calc_bulgaria,
    rules={
        "multipliers": {
            "physical": [2, 4, 8, 5, 10, 9, 7, 3, 6],
            "foreigner": [21, 19, 17, 13, 11, 9, 7, 3, 1],
            "miscellaneous": [4, 3, 2, 7, 6, 5, 4, 3, 2],
        },
        "regex": [re.compile(r"^(BG)(\d{9,10})$")],
    },
)
