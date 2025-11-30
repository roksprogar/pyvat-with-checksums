import re
from ..core import Country

def calc_italy(vat: str) -> bool:
    if int(vat[:7]) == 0:
        return False
        
    temp = int(vat[7:10])
    if temp < 1 or (temp > 201 and temp != 999 and temp != 888):
        return False
        
    total = 0
    multipliers = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
    
    for i in range(10):
        temp = int(vat[i]) * multipliers[i]
        if temp > 9:
            total += (temp // 10) + (temp % 10)
        else:
            total += temp
            
    total = 10 - (total % 10)
    if total > 9:
        total = 0
        
    expect = int(vat[10])
    return total == expect

italy = Country(
    name='Italy',
    codes=['IT', 'ITA', '380'],
    calc_fn=calc_italy,
    rules={
        'regex': [re.compile(r'^(IT)(\d{11})$')]
    }
)
