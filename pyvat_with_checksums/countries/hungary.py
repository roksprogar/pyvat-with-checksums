import re
from ..core import Country


def calc_hungary(vat: str) -> bool:
    total = 0
    multipliers = [9, 7, 3, 1, 9, 7, 3]

    for i in range(7):
        total += int(vat[i]) * multipliers[i]

    total = 10 - (total % 10)
    if total == 10:
        total = 0

    expect = int(vat[7])
    return total == expect


hungary = Country(
    name="Hungary",
    codes=["HU", "HUN", "348"],
    calc_fn=calc_hungary,
    rules={"regex": [re.compile(r"^(HU)(\d{8})$")]},
)
