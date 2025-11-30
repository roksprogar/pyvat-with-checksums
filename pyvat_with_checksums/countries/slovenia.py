import re
from ..core import Country


def calc_slovenia(vat: str) -> bool:
    total = 0
    multipliers = slovenia.rules["multipliers"]["common"]

    for i in range(7):
        total += int(vat[i]) * multipliers[i]

    total = 11 - (total % 11)
    if total == 10:
        total = 0

    expect = int(vat[7])
    return total != 11 and total == expect


slovenia = Country(
    name="Slovenia",
    codes=["SI", "SVN", "705"],
    calc_fn=calc_slovenia,
    rules={
        "multipliers": {"common": [8, 7, 6, 5, 4, 3, 2]},
        "regex": [re.compile(r"^(SI)([1-9]\d{7})$")],
    },
)
