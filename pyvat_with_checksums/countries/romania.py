import re
from ..core import Country

def calc_romania(vat: str) -> bool:
    total = 0
    vat_length = len(vat)
    multipliers = romania.rules['multipliers']['common'][10 - vat_length:]
    
    for i in range(vat_length - 1):
        total += int(vat[i]) * multipliers[i]
        
    total = (10 * total) % 11
    if total == 10:
        total = 0
        
    expect = int(vat[vat_length - 1])
    return total == expect

romania = Country(
    name='Romania',
    codes=['RO', 'ROU', '642'],
    calc_fn=calc_romania,
    rules={
        'multipliers': {
            'common': [7, 5, 3, 2, 1, 7, 5, 3, 2]
        },
        'regex': [re.compile(r'^(RO)([1-9]\d{1,9})$')]
    }
)
