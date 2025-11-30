import re
from ..core import Country


def calc_switzerland(vat: str) -> bool:
    total = 0
    multipliers = switzerland.rules["multipliers"]["common"]

    for i in range(8):
        total += int(vat[i]) * multipliers[i]

    total = 11 - (total % 11)
    if total == 10:
        return False
    if total == 11:
        total = 0

    expect = int(vat[8])
    return total == expect


switzerland = Country(
    name="Switzerland",
    codes=["CH", "CHE", "756"],
    calc_fn=calc_switzerland,
    rules={
        "multipliers": {"common": [5, 4, 3, 2, 7, 6, 5, 4]},
        "regex": [re.compile(r"^(CHE)(\d{9})(MWST|TVA|IVA)?$")],
    },
)
