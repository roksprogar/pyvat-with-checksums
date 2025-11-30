import re
from ..core import Country


def get_char_value(char: str) -> int:
    if char == "+":
        return 36
    if char == "*":
        return 37

    code = ord(char) - 55
    if 9 < code < 91:
        return code

    return int(char)


def mod97(value: str) -> int:
    res = 0
    for char in value:
        res = (res * 10 + int(char)) % 97
    return res


def is_ninety_seven_mod(value: str) -> bool:
    return mod97(value) == 1


def calc_netherlands(vat: str) -> bool:
    vat_clean = vat.replace(" ", "").replace("-", "").replace("_", "").upper()
    additional = netherlands.rules["additional"][0]

    match = additional.match(vat_clean)
    if not match:
        return False

    numb = match.group(1)

    # Calculate character values for mod97 check
    char_values_str = "".join(str(get_char_value(c)) for c in f"NL{vat_clean}")

    # Mod 11 check
    total = 0
    multipliers = netherlands.rules["multipliers"]["common"]
    for i in range(8):
        total += int(numb[i]) * multipliers[i]

    total = total % 11
    if total > 9:
        total = 0

    expect = int(numb[8])

    return total == expect or is_ninety_seven_mod(char_values_str)


netherlands = Country(
    name="Netherlands",
    codes=["NL", "NLD", "528"],
    calc_fn=calc_netherlands,
    rules={
        "multipliers": {"common": [9, 8, 7, 6, 5, 4, 3, 2]},
        "regex": [re.compile(r"^(NL)(\d{9}B\d{2})$")],
        "additional": [re.compile(r"^(\d{9})B\d{2}$")],
    },
)
