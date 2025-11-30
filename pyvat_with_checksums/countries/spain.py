import re
from typing import List
from ..core import Country

def _extract_digit_and_multiply(vat: str, multipliers: List[int], total: int) -> int:
    result = total
    for i in range(7):
        temp = int(vat[i + 1]) * multipliers[i]
        if temp > 9:
            result += (temp // 10) + (temp % 10)
        else:
            result += temp
    return result

def _is_national_juridical_entities(vat: str, multipliers: List[int]) -> bool:
    total = _extract_digit_and_multiply(vat, multipliers, 0)
    total = 10 - (total % 10)
    if total == 10:
        total = 0
    expect = int(vat[8])
    return total == expect

def _is_non_national_juridical(vat: str, multipliers: List[int]) -> bool:
    total = _extract_digit_and_multiply(vat, multipliers, 0)
    total = 10 - (total % 10)
    total_str = chr(total + 64)
    expect = vat[8]
    return total_str == expect

def _is_personal_y_to_z(vat: str) -> bool:
    temp_number = vat
    if temp_number[0] == 'Y':
        temp_number = '1' + temp_number[1:]
    elif temp_number[0] == 'Z':
        temp_number = '2' + temp_number[1:]
        
    expect = 'TRWAGMYFPDXBNJZSQVHLCKE'[int(temp_number[:8]) % 23]
    return temp_number[8] == expect

def _is_personal_k_to_x(vat: str) -> bool:
    expect = 'TRWAGMYFPDXBNJZSQVHLCKE'[int(vat[1:8]) % 23]
    return vat[8] == expect

def calc_spain(vat: str) -> bool:
    additional = spain.rules['additional']
    multipliers = spain.rules['multipliers']['common']
    
    if additional[0].match(vat):
        return _is_national_juridical_entities(vat, multipliers)
        
    if additional[1].match(vat):
        return _is_non_national_juridical(vat, multipliers)
        
    if additional[2].match(vat):
        return _is_personal_y_to_z(vat)
        
    if additional[3].match(vat):
        return _is_personal_k_to_x(vat)
        
    return False

spain = Country(
    name='Spain',
    codes=['ES', 'ESP', '724'],
    calc_fn=calc_spain,
    rules={
        'multipliers': {
            'common': [2, 1, 2, 1, 2, 1, 2]
        },
        'regex': [
            re.compile(r'^(ES)([A-Z]\d{8})$'),
            re.compile(r'^(ES)([A-HN-SW]\d{7}[A-J])$'),
            re.compile(r'^(ES)([0-9YZ]\d{7}[A-Z])$'),
            re.compile(r'^(ES)([KLMX]\d{7}[A-Z])$')
        ],
        'additional': [
            re.compile(r'^[A-H|J|U|V]\d{8}$'),
            re.compile(r'^[A-H|N-S|W]\d{7}[A-J]$'),
            re.compile(r'^[0-9|Y|Z]\d{7}[A-Z]$'),
            re.compile(r'^[K|L|M|X]\d{7}[A-Z]$')
        ]
    }
)
