import re
from typing import List
from ..core import Country

def generate_check_sums(numbers: List[int], validators: List[int]) -> List[int]:
    initial_check_sums = [0, 0]
    checker_a = 0
    checker_b = 0
    
    for index, validator in enumerate(validators):
        if index > 0:
            checker_a += numbers[index - 1] * validator
        checker_b += numbers[index] * validator
        
    return [checker_a, checker_b]

def is_repeated_array(numbers: List[int]) -> bool:
    if not numbers:
        return False
    first = numbers[0]
    return all(n == first for n in numbers)

def get_remaining(value: int) -> int:
    return 0 if value % 11 < 2 else 11 - (value % 11)

def calc_brazil(vat: str) -> bool:
    # Remove non-digits just in case, though regex should handle it
    # But calc_fn receives the "number" part.
    # For Brazil, the regex captures: (BR)?(\d{14}|\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2})
    # So group 2 is the number part which might contain dots/slashes/dashes if not stripped.
    # However, core.py removes extra chars before calling calc_fn?
    # Wait, core.py: clean_vat = remove_extra_chars(vat)
    # remove_extra_chars removes space, -, ., /
    # So clean_vat is alphanumeric.
    # For Brazil, regex is applied to clean_vat?
    # jsvat regex: /^(BR)?(\d{14}|\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2})$/
    # If clean_vat is used, the dots/slashes are gone.
    # So the regex in python should probably match the clean version if we clean it first.
    # But jsvat seems to apply regex to the input?
    # Let's check jsvat core logic again.
    # jsvat.ts: const cleanVAT = removeExtraChars(vat);
    # Then isVatValidToRegexp(cleanVAT, ...)
    # So regex must match cleanVAT.
    # But Brazil regex in jsvat has dots/slashes.
    # /^(BR)?(\d{14}|\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2})$/
    # If cleanVAT has no dots, this regex part \d{2}\.\d{3}... will fail.
    # But \d{14} will match.
    # So for Brazil, cleanVAT will be just digits (and maybe BR).
    
    numbers = [int(d) for d in vat if d.isdigit()]
    
    if is_repeated_array(numbers):
        return False
        
    validators = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    checkers = generate_check_sums(numbers, validators)
    
    return numbers[12] == get_remaining(checkers[0]) and numbers[13] == get_remaining(checkers[1])

brazil = Country(
    name='Brazil',
    codes=['BR', 'BRA', '076'],
    calc_fn=calc_brazil,
    rules={
        'regex': [re.compile(r'^(BR)?(\d{14})$')] # Adjusted for clean VAT
    },
    vat_starts_with_country_code=False
)
