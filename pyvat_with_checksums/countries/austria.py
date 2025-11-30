import re
from ..core import Country

def calc_austria(vat: str) -> bool:
    total = 0
    multipliers = [1, 2, 1, 2, 1, 2, 1]
    
    for i in range(7):
        temp = int(vat[i]) * multipliers[i]
        
        if temp > 9:
            total += (temp // 10) + (temp % 10)
        else:
            total += temp
            
    total = 10 - ((total + 4) % 10)
    if total == 10:
        total = 0
        
    return total == int(vat[7])

austria = Country(
    name='Austria',
    codes=['AT', 'AUT', '040'],
    calc_fn=calc_austria,
    rules={
        'regex': [re.compile(r'^(AT)U(\d{8})$')]
    }
)
