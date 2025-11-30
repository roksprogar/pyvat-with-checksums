import re
from typing import List
from ..core import Country

def _check_10_digit_inn(vat: str, multipliers: List[int]) -> bool:
    if len(vat) == 10:
        total = 0
        for i in range(10):
            total += int(vat[i]) * multipliers[i]
            
        total = total % 11
        if total > 9:
            total = total % 10
            
        expect = int(vat[9])
        return total == expect
    return False

def _check_12_digit_inn(vat: str, multipliers_m2: List[int], multipliers_m3: List[int]) -> bool:
    if len(vat) == 12:
        total1 = 0
        for j in range(11):
            total1 += int(vat[j]) * multipliers_m2[j]
            
        total1 = total1 % 11
        if total1 > 9:
            total1 = total1 % 10
            
        total2 = 0
        for k in range(11):
            total2 += int(vat[k]) * multipliers_m3[k]
            
        total2 = total2 % 11
        if total2 > 9:
            total2 = total2 % 10
            
        expect1 = (total1 == int(vat[10]))
        expect2 = (total2 == int(vat[11]))
        return expect1 and expect2
    return False

def calc_russia(vat: str) -> bool:
    multipliers = russia.rules['multipliers']
    return (
        _check_10_digit_inn(vat, multipliers['m_1']) or
        _check_12_digit_inn(vat, multipliers['m_2'], multipliers['m_3'])
    )

russia = Country(
    name='Russian Federation',
    codes=['RU', 'RUS', '643'],
    calc_fn=calc_russia,
    rules={
        'multipliers': {
            'm_1': [2, 4, 10, 3, 5, 9, 4, 6, 8, 0],
            'm_2': [7, 2, 4, 10, 3, 5, 9, 4, 6, 8, 0],
            'm_3': [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8, 0]
        },
        'regex': [re.compile(r'^(RU)(\d{10}|\d{12})$')]
    }
)
