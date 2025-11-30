import re
from ..core import Country

def calc_estonia(vat: str) -> bool:
    total = 0
    multipliers = [3, 7, 1, 3, 7, 1, 3, 7]
    
    for i in range(8):
        total += int(vat[i]) * multipliers[i]
        
    total = 10 - (total % 10)
    if total == 10:
        total = 0
        
    expect = int(vat[8])
    return total == expect

estonia = Country(
    name='Estonia',
    codes=['EE', 'EST', '233'],
    calc_fn=calc_estonia,
    rules={
        'regex': [re.compile(r'^(EE)(10\d{7})$')]
    }
)
