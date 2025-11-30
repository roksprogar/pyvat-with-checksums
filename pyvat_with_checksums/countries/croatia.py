import re
from ..core import Country

def calc_croatia(vat: str) -> bool:
    product = 10
    sum_val = 0
    
    for i in range(10):
        sum_val = (int(vat[i]) + product) % 10
        if sum_val == 0:
            sum_val = 10
        product = (2 * sum_val) % 11
        
    expect = int(vat[10])
    return (product + expect) % 10 == 1

croatia = Country(
    name='Croatia',
    codes=['HR', 'HRV', '191'],
    calc_fn=calc_croatia,
    rules={
        'regex': [re.compile(r'^(HR)(\d{11})$')]
    }
)
