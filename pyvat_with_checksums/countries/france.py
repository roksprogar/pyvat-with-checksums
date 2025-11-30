import re
from ..core import Country

def calc_france(vat: str) -> bool:
    if not re.match(r'^\d{11}$', vat):
        return True
        
    total = int(vat[2:])
    total = (total * 100 + 12) % 97
    
    expect = int(vat[:2])
    return total == expect

france = Country(
    name='France',
    codes=['FR', 'FRA', '250'],
    calc_fn=calc_france,
    rules={
        'regex': [
            re.compile(r'^(FR)(\d{11})$'),
            re.compile(r'^(FR)([A-HJ-NP-Z]\d{10})$'),
            re.compile(r'^(FR)(\d[A-HJ-NP-Z]\d{9})$'),
            re.compile(r'^(FR)([A-HJ-NP-Z]{2}\d{9})$')
        ]
    }
)
