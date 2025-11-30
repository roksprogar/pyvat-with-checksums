import re
from ..core import Country


def calc_norway(vat: str) -> bool:
    total = 0
    multipliers = norway.rules["multipliers"]["common"]

    for i in range(8):
        total += int(vat[i]) * multipliers[i]

    total = 11 - (total % 11)
    if total == 11:
        total = 0

    if total < 10:
        expect = int(vat[8])
        return total == expect

    return False


norway = Country(
    name="Norway",
    codes=["NO", "NOR", "578"],
    calc_fn=calc_norway,
    rules={
        "multipliers": {"common": [3, 2, 7, 6, 5, 4, 3, 2]},
        "regex": [re.compile(r"^(NO)(\d{9})(MVA)?$")],
    },
)
