import re
from ..core import Country


def calc_portugal(vat: str) -> bool:
    total = 0
    multipliers = portugal.rules["multipliers"]["common"]

    for i in range(8):
        total += int(vat[i]) * multipliers[i]

    total = 11 - (total % 11)
    if total > 9:
        total = 0

    expect = int(vat[8])
    return total == expect


portugal = Country(
    name="Portugal",
    codes=["PT", "PRT", "620"],
    calc_fn=calc_portugal,
    rules={
        "multipliers": {"common": [9, 8, 7, 6, 5, 4, 3, 2]},
        "regex": [re.compile(r"^(PT)(\d{9})$")],
    },
)
