import re
from ..core import Country


def calc_malta(vat: str) -> bool:
    total = 0
    multipliers = [3, 4, 6, 7, 8, 9]

    for i in range(6):
        total += int(vat[i]) * multipliers[i]

    total = 37 - (total % 37)
    expect = int(vat[6:8])
    return total == expect


malta = Country(
    name="Malta",
    codes=["MT", "MLT", "470"],
    calc_fn=calc_malta,
    rules={"regex": [re.compile(r"^(MT)([1-9]\d{7})$")]},
)
