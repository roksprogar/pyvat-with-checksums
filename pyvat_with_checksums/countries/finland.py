import re
from ..core import Country

def calc_finland(vat: str) -> bool:
    total = 0
    multipliers = [7, 9, 10, 5, 8, 4, 2]
    
    for i in range(7):
        total += int(vat[i]) * multipliers[i]
        
    total = 11 - (total % 11)
    if total > 9:
        total = 0
        
    expect = int(vat[7])
    return total == expect

finland = Country(
    name='Finland',
    codes=['FI', 'FIN', '246'],
    calc_fn=calc_finland,
    rules={
        'regex': [re.compile(r'^(FI)(\d{8})$')]
    }
)
