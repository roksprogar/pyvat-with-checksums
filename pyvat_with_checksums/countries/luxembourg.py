import re
from ..core import Country


def calc_luxembourg(vat: str) -> bool:
    expect = int(vat[6:8])
    check_digit = int(vat[:6]) % 89
    return check_digit == expect


luxembourg = Country(
    name="Luxembourg",
    codes=["LU", "LUX", "442"],
    calc_fn=calc_luxembourg,
    rules={"regex": [re.compile(r"^(LU)(\d{8})$")]},
)
