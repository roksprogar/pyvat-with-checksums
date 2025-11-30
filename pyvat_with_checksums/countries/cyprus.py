import re
from ..core import Country

def extract_and_multiply_by_counter(vat: str, total: int) -> int:
    result = total
    for i in range(8):
        temp = int(vat[i])
        if i % 2 == 0:
            if temp == 0:
                temp = 1
            elif temp == 1:
                temp = 0
            elif temp == 2:
                temp = 5
            elif temp == 3:
                temp = 7
            elif temp == 4:
                temp = 9
            else:
                temp = temp * 2 + 3
        result += temp
    return result

def calc_cyprus(vat: str) -> bool:
    if int(vat[:2]) == 12:
        return False
        
    total = extract_and_multiply_by_counter(vat, 0)
    total = total % 26
    total_char = chr(total + 65)
    
    expect = vat[8]
    return total_char == expect

cyprus = Country(
    name='Cyprus',
    codes=['CY', 'CYP', '196'],
    calc_fn=calc_cyprus,
    rules={
        'regex': [re.compile(r'^(CY)([0-59]\d{7}[A-Z])$')]
    }
)
