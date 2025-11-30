import re
from ..core import Country

def calc_denmark(vat: str) -> bool:
    total = 0
    multipliers = [2, 7, 6, 5, 4, 3, 2, 1]
    
    for i in range(8):
        total += int(vat[i]) * multipliers[i]
        
    return total % 11 == 0

denmark = Country(
    name='Denmark',
    codes=['DK', 'DNK', '208'],
    calc_fn=calc_denmark,
    rules={
        'regex': [re.compile(r'^(DK)(\d{8})$')]
    }
)
