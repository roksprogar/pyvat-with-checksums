import re
from ..core import Country

def calc_europe(vat: str) -> bool:
    return True

europe = Country(
    name='Europe',
    codes=['EU', 'EUR', '000'],
    calc_fn=calc_europe,
    rules={
        'regex': [re.compile(r'^(EU)(\d{9})$')]
    }
)
