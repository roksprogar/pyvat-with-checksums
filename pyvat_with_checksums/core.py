from typing import List, Optional, Dict, Union, Callable, Iterator, Any
import re
from dataclasses import dataclass


@dataclass
class Country:
    name: str
    codes: List[str]
    calc_fn: Callable[[str], bool]
    rules: Dict[str, Any]
    vat_starts_with_country_code: bool = True


@dataclass
class VatCheckResult:
    value: Optional[str]
    is_valid: bool
    is_valid_format: bool
    is_supported_country: bool
    country: Optional[Country] = None


def remove_extra_chars(vat: str) -> str:
    return re.sub(r"(\s|-|\.|\/)+", "", str(vat).upper())


def is_vat_valid_to_regexp(
    vat: str, regex_arr: List[re.Pattern]
) -> Dict[str, Union[bool, Optional[re.Pattern]]]:
    for regex in regex_arr:
        if regex.match(vat):
            return {"is_valid": True, "regex": regex}
    return {"is_valid": False, "regex": None}


def is_vat_valid(vat: str, country: Country) -> bool:
    regexp_valid_res = is_vat_valid_to_regexp(vat, country.rules["regex"])
    if not regexp_valid_res["is_valid"] or not regexp_valid_res["regex"]:
        return False

    match = regexp_valid_res["regex"].match(vat)
    if not match:
        return False

    # The regex usually captures the country code in group 1 and the number in group 2
    # We pass the number part to the calc function
    # For Brazil, group 1 is optional (BR)?, group 2 is the number.
    return country.calc_fn(match.group(2))


def get_countries(vat: str, countries_list: List[Country]) -> Iterator[Country]:
    for country in countries_list:
        # Check if starts with country code
        for code in country.codes:
            if vat.startswith(code):
                yield country
                break

        # Check if country allows VAT without code prefix and VAT starts with number
        if not country.vat_starts_with_country_code and re.match(r"^\d{2}", vat):
            yield country


def get_country(vat: str, countries_list: List[Country]) -> Optional[Country]:
    # Returns the first matching country, for backward compatibility or simple use cases
    return next(get_countries(vat, countries_list), None)


def check_vat(vat: str, countries_list: List[Country] = None) -> VatCheckResult:
    if countries_list is None:
        from .countries import all_countries

        countries_list = all_countries

    if not vat:
        return VatCheckResult(
            value=None,
            is_valid=False,
            is_valid_format=False,
            is_supported_country=False,
            country=None,
        )

    clean_vat = remove_extra_chars(vat)

    # Iterate through all candidate countries
    best_result = None

    for country in get_countries(clean_vat, countries_list):
        is_valid = is_vat_valid(clean_vat, country)
        is_valid_format = is_vat_valid_to_regexp(clean_vat, country.rules["regex"])[
            "is_valid"
        ]

        result = VatCheckResult(
            value=clean_vat,
            is_valid=is_valid,
            is_valid_format=is_valid_format,
            is_supported_country=True,
            country=country,
        )

        if is_valid:
            return result

        if best_result is None:
            best_result = result

    if best_result:
        return best_result

    return VatCheckResult(
        value=clean_vat,
        is_valid=False,
        is_valid_format=False,
        is_supported_country=False,
        country=None,
    )
