import re
from ..core import Country

def calc_ireland(vat: str) -> bool:
    type_formats = ireland.rules['type_formats']
    multipliers = ireland.rules['multipliers']
    
    new_vat = vat
    if type_formats['first'].match(vat):
        new_vat = '0' + vat[2:7] + vat[:1] + vat[7:8]
        
    total = 0
    for i in range(7):
        total += int(new_vat[i]) * multipliers['common'][i]
        
    if type_formats['third'].match(new_vat):
        total += 72 if new_vat[8] == 'H' else 9
        
    total = total % 23
    if total == 0:
        total_char = 'W'
    else:
        total_char = chr(total + 64)
        
    expect = new_vat[7]
    return total_char == expect

ireland = Country(
    name='Ireland',
    codes=['IE', 'IRL', '372'],
    calc_fn=calc_ireland,
    rules={
        'multipliers': {
            'common': [8, 7, 6, 5, 4, 3, 2]
        },
        'type_formats': {
            'first': re.compile(r'^\d[A-Z*+]'),
            'third': re.compile(r'^\d{7}[A-Z][AH]$')
        },
        'regex': [
            re.compile(r'^(IE)(\d{7}[A-W])$'),
            re.compile(r'^(IE)([7-9][A-Z*+)]\d{5}[A-W])$'),
            re.compile(r'^(IE)(\d{7}[A-W][AH])$')
        ]
    }
)
