import re
from ..core import Country

def calc_belgium(vat: str) -> bool:
    new_vat = '0' + vat if len(vat) == 9 else vat
    
    if int(new_vat[1]) == 0:
        return False
        
    check = 97 - (int(new_vat[:8]) % 97)
    return check == int(new_vat[8:10])

belgium = Country(
    name='Belgium',
    codes=['BE', 'BEL', '056'],
    calc_fn=calc_belgium,
    rules={
        'regex': [re.compile(r'^(BE)(0?\d{9})$')]
    }
)
