import re
from ..core import Country


def calc_latvia(vat: str) -> bool:
    if re.match(r"^[0-3]", vat):
        return bool(re.match(r"^[0-3][0-9][0-1][0-9]", vat))
    else:
        total = 0
        multipliers = [9, 1, 4, 8, 3, 10, 2, 5, 7, 6]

        for i in range(10):
            total += int(vat[i]) * multipliers[i]

        if total % 11 == 4 and int(vat[0]) == 9:
            total = total - 45

        if total % 11 == 4:
            total = 4 - (total % 11)
        elif total % 11 > 4:
            total = 14 - (total % 11)
        elif total % 11 < 4:
            total = 3 - (total % 11)

        expect = int(vat[10])
        return total == expect


latvia = Country(
    name="Latvia",
    codes=["LV", "LVA", "428"],
    calc_fn=calc_latvia,
    rules={"regex": [re.compile(r"^(LV)(\d{11})$")]},
)
