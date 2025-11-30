import re
from typing import List
from ..core import Country

def _extract_digit(vat: str, multiplier_list: List[int], key: int) -> int:
    return int(vat[key]) * multiplier_list[key]

def _double_check_calculation(vat: str, total: int, multipliers: List[int]) -> int:
    result = total
    if result % 11 == 10:
        result = 0
        for i in range(8):
            result += _extract_digit(vat, multipliers, i)
    return result

def _extract_digit_simple(vat: str, total: int) -> int:
    result = total
    for i in range(8):
        result += int(vat[i]) * (i + 1)
    return result

def _check_digit(total: int) -> int:
    result = total % 11
    if result == 10:
        result = 0
    return result

def _check_9_digit_vat(vat: str, multipliers_short: List[int]) -> bool:
    if len(vat) == 9:
        if not re.match(r'^\d{7}1', vat):
            return False
            
        total = _extract_digit_simple(vat, 0)
        total = _double_check_calculation(vat, total, multipliers_short)
        total = _check_digit(total)
        
        expect = int(vat[8])
        return total == expect
    return False

def _extract_digit_12(vat: str, total: int, multipliers_med: List[int]) -> int:
    result = total
    for k in range(11):
        result += _extract_digit(vat, multipliers_med, k)
    return result

def _double_check_calculation_12(vat: str, total: int, multipliers_alt: List[int]) -> int:
    result = total
    if total % 11 == 10:
        result = 0
        for idx in range(11):
            result += _extract_digit(vat, multipliers_alt, idx)
    return result

def _check_12_digit_vat(vat: str, multipliers_med: List[int], multipliers_alt: List[int]) -> bool:
    if len(vat) == 12:
        if not re.match(r'^\d{10}1', vat):
            return False
            
        total = _extract_digit_12(vat, 0, multipliers_med)
        total = _double_check_calculation_12(vat, total, multipliers_alt)
        total = _check_digit(total)
        
        expect = int(vat[11])
        return total == expect
    return False

def calc_lithuania(vat: str) -> bool:
    multipliers = lithuania.rules['multipliers']
    return (
        _check_9_digit_vat(vat, multipliers['short']) or
        _check_12_digit_vat(vat, multipliers['med'], multipliers['alt'])
    )

lithuania = Country(
    name='Lithuania',
    codes=['LT', 'LTU', '440'],
    calc_fn=calc_lithuania,
    rules={
        'multipliers': {
            'short': [3, 4, 5, 6, 7, 8, 9, 1],
            'med': [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2],
            'alt': [3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4]
        },
        'regex': [re.compile(r'^(LT)(\d{9}|\d{12})$')]
    }
)
