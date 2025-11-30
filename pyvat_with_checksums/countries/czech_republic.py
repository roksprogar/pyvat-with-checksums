import re
import math
from typing import List, Optional
from ..core import Country


def is_legal_entities(
    vat: str, multipliers: List[int], additional: List[re.Pattern]
) -> bool:
    total = 0
    if additional[0].match(vat):
        for i in range(7):
            total += int(vat[i]) * multipliers[i]

        total = 11 - (total % 11)
        if total == 10:
            total = 0
        if total == 11:
            total = 1

        expect = int(vat[7])
        return total == expect
    return False


def is_individual_type1(vat: str, additional: List[re.Pattern]) -> bool:
    if additional[1].match(vat):
        return int(vat[:2]) <= 62
    return False


def is_individual_type2(
    vat: str,
    multipliers: List[int],
    additional: List[re.Pattern],
    lookup: Optional[List[int]],
) -> bool:
    total = 0
    if additional[2].match(vat):
        for j in range(7):
            total += int(vat[j + 1]) * multipliers[j]

        if total % 11 == 0:
            a = total + 11
        else:
            a = math.ceil(total / 11) * 11

        pointer = a - total - 1

        expect = int(vat[8])
        if not lookup:
            return False
        return lookup[pointer] == expect
    return False


def is_individual_type3(vat: str, additional: List[re.Pattern]) -> bool:
    if additional[3].match(vat):
        temp = (
            int(vat[:2]) + int(vat[2:4]) + int(vat[4:6]) + int(vat[6:8]) + int(vat[8:])
        )
        expect = int(vat) % 11 == 0
        return (temp % 11 == 0) and expect
    return False


def calc_czech_republic(vat: str) -> bool:
    multipliers = czech_republic.rules["multipliers"]
    additional = czech_republic.rules["additional"]
    lookup = czech_republic.rules.get("lookup")

    if not additional:
        return False

    return (
        is_legal_entities(vat, multipliers["common"], additional)
        or is_individual_type2(vat, multipliers["common"], additional, lookup)
        or is_individual_type3(vat, additional)
        or is_individual_type1(vat, additional)
    )


czech_republic = Country(
    name="Czech Republic",
    codes=["CZ", "CZE", "203"],
    calc_fn=calc_czech_republic,
    rules={
        "multipliers": {"common": [8, 7, 6, 5, 4, 3, 2]},
        "lookup": [8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8],
        "regex": [re.compile(r"^(CZ)(\d{8,10})(\d{3})?$")],
        "additional": [
            re.compile(r"^\d{8}$"),
            re.compile(r"^[0-5][0-9][0|1|5|6]\d[0-3]\d\d{3}$"),
            re.compile(r"^6\d{8}$"),
            re.compile(r"^\d{2}[0-3|5-8]\d[0-3]\d\d{4}$"),
        ],
    },
)
