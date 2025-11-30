import re
from ..core import Country

def calc_greece(vat: str) -> bool:
    new_vat = '0' + vat if len(vat) == 8 else vat
    total = 0
    multipliers = [256, 128, 64, 32, 16, 8, 4, 2]
    
    for i in range(8):
        total += int(new_vat[i]) * multipliers[i]
        
    total = total % 11
    if total > 9:
        total = 0
        
    expect = int(new_vat[8])
    return total == expect

greece = Country(
    name='Greece',
    codes=['GR', 'GRC', '300', 'EL'],
    calc_fn=calc_greece,
    rules={
        'regex': [re.compile(r'^(EL)(\d{9})$')]
    }
)
