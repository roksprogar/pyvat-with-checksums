import re
from ..core import Country

def calc_poland(vat: str) -> bool:
    total = 0
    multipliers = poland.rules['multipliers']['common']
    
    for i in range(9):
        total += int(vat[i]) * multipliers[i]
        
    total = total % 11
    if total > 9:
        total = 0
        
    expect = int(vat[9])
    return total == expect

poland = Country(
    name='Poland',
    codes=['PL', 'POL', '616'],
    calc_fn=calc_poland,
    rules={
        'multipliers': {
            'common': [6, 5, 7, 2, 3, 4, 5, 6, 7]
        },
        'regex': [re.compile(r'^(PL)(\d{10})$')]
    }
)
