import re
from ..core import Country


def calc_slovakia_republic(vat: str) -> bool:
    check_digit = int(vat) % 11
    return check_digit == 0


slovakia_republic = Country(
    name="Slovakia Republic",
    codes=["SK", "SVK", "703"],
    calc_fn=calc_slovakia_republic,
    rules={"regex": [re.compile(r"^(SK)([1-9]\d[2346-9]\d{7})$")]},
)
