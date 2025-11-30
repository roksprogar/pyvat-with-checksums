import re
from ..core import Country


def calc_sweden(vat: str) -> bool:
    r = 0
    for i in range(0, 9, 2):
        digit = int(vat[i])
        r += (digit // 5) + ((digit * 2) % 10)

    s = 0
    for j in range(1, 9, 2):
        s += int(vat[j])

    check_digit = (10 - ((r + s) % 10)) % 10
    expect = int(vat[9])

    return check_digit == expect


sweden = Country(
    name="Sweden",
    codes=["SE", "SWE", "752"],
    calc_fn=calc_sweden,
    rules={"regex": [re.compile(r"^(SE)(\d{10}01)$")]},
)
