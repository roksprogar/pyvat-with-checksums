import re
from ..core import Country


def calc_andorra(vat: str) -> bool:
    return len(vat) == 8


andorra = Country(
    name="Andorra",
    codes=["AD", "AND", "020"],
    calc_fn=calc_andorra,
    rules={
        "regex": [
            re.compile(
                r"^(AD)([fealecdgopuFEALECDGOPU]{1}\d{6}[fealecdgopuFEALECDGOPU]{1})$"
            )
        ]
    },
)
