import re
from ..core import Country

def calc_germany(vat: str) -> bool:
    product = 10
    
    for i in range(8):
        sum_val = (int(vat[i]) + product) % 10
        if sum_val == 0:
            sum_val = 10
        product = (2 * sum_val) % 11
        
    if 11 - product == 10:
        check_digit = 0
    else:
        check_digit = 11 - product
        
    return check_digit == int(vat[8])

germany = Country(
    name='Germany',
    codes=['DE', 'DEU', '276'],
    calc_fn=calc_germany,
    rules={
        'regex': [re.compile(r'^(DE)([1-9]\d{8})$')]
    }
)
