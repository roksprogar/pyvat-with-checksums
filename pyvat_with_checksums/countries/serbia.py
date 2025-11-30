import re
from ..core import Country

def calc_serbia(vat: str) -> bool:
    product = 10
    sum_val = 0
    
    for i in range(8):
        sum_val = (int(vat[i]) + product) % 10
        if sum_val == 0:
            sum_val = 10
        product = (2 * sum_val) % 11
        
    expect = 1
    check_digit = (product + int(vat[8])) % 10
    return check_digit == expect

serbia = Country(
    name='Serbia',
    codes=['RS', 'SRB', '688'],
    calc_fn=calc_serbia,
    rules={
        'regex': [re.compile(r'^(RS)(\d{9})$')]
    }
)
