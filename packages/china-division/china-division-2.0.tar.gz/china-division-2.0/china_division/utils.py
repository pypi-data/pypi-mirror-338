# china_division/utils.py
import re
from typing import Dict, List, Optional, Tuple, Set
from .data import DIVISION_DATA, MUNICIPALITIES


def is_municipality(code: str) -> bool:
    return code in MUNICIPALITIES


def get_division_level(code: str) -> str:
    if not code or len(code) != 6 or not code.isdigit():
        return 'invalid'
    if code.endswith('0000'):
        return 'province'
    elif code.endswith('00'):
        return 'city'
    else:
        return 'county'


def get_parent_code(code: str) -> Optional[str]:
    level = get_division_level(code)
    if level == 'province':
        return None
    elif level == 'city':
        return code[:2] + '0000'
    else:
        return code[:4] + '00'


def get_full_name(code: str) -> str:
    if not code or code not in DIVISION_DATA:
        return ''

    level = get_division_level(code)
    name = DIVISION_DATA[code]

    if level == 'province':
        return name
    elif level == 'city':
        province_code = get_parent_code(code)
        return f"{DIVISION_DATA.get(province_code, '')}{name}"
    else:
        city_code = get_parent_code(code)
        province_code = get_parent_code(city_code) if city_code else None
        parts = []
        if province_code and province_code in DIVISION_DATA:
            parts.append(DIVISION_DATA[province_code])
        if city_code and city_code in DIVISION_DATA:
            parts.append(DIVISION_DATA[city_code])
        parts.append(name)
        return ''.join(parts)


def normalize_query(query: str) -> str:
    return re.sub(r'[^\u4e00-\u9fff]', '', query)


def build_search_index() -> Dict[str, Set[str]]:
    index = {}
    for code in DIVISION_DATA:
        full_name = get_full_name(code)
        for char in full_name:
            if char not in index:
                index[char] = set()
            index[char].add(code)
    return index


SEARCH_INDEX = build_search_index()


def find_divisions_by_chars(chars: str) -> Set[str]:
    result = None
    for char in chars:
        if char in SEARCH_INDEX:
            if result is None:
                result = SEARCH_INDEX[char].copy()
            else:
                result.intersection_update(SEARCH_INDEX[char])
        else:
            return set()
    return result if result is not None else set()


def hierarchical_search(query: str) -> List[Tuple[str, str]]:
    normalized = normalize_query(query)
    if not normalized:
        return []

    max_len = len(normalized)

    for length in range(max_len, 0, -1):
        matched_codes = find_divisions_by_chars(normalized[:length])

        if matched_codes:
            remaining = normalized[length:]
            if remaining:
                final_codes = set()
                for code in matched_codes:
                    full_name = get_full_name(code)
                    if remaining in full_name:
                        final_codes.add(code)

                if final_codes:
                    return [(code, get_full_name(code)) for code in final_codes]
            else:
                return [(code, get_full_name(code)) for code in matched_codes]

    return []


# 新增的函数
def get_child_divisions(code: str) -> List[Tuple[str, str]]:
    """获取下级行政区划"""
    level = get_division_level(code)
    if level == 'county':
        return []

    prefix = code[:2] if level == 'province' else code[:4]
    suffix = '00' if level == 'province' else ''

    children = []
    for child_code, name in DIVISION_DATA.items():
        if child_code.startswith(prefix) and child_code != code:
            if level == 'province' and child_code.endswith('00'):
                children.append((child_code, name))
            elif level == 'city' and not child_code.endswith('00'):
                children.append((child_code, name))

    return children