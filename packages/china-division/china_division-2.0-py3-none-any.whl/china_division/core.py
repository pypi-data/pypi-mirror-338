# china_division/core.py
from typing import Union, List, Tuple, Optional
from .utils import (
    hierarchical_search,
    get_full_name,
    get_parent_code,
    get_child_divisions
)
from .data import DIVISION_DATA


def get_division_info(code: str) -> Union[str, None]:
    if code not in DIVISION_DATA:
        return None
    return get_full_name(code)


def search_division(query: str) -> str:
    """
    搜索行政区划，总是返回字符串形式
    多个结果时用"|"分隔（代码和名称用":"分隔）
    例如: "150421:内蒙古自治区赤峰市阿鲁科尔沁旗|210302:辽宁省鞍山市铁东区"
    """
    if not query:
        return "未找到对应的行政区划信息"

    # 代码查询
    if query in DIVISION_DATA:
        info = get_division_info(query)
        return info if info else "未找到对应的行政区划信息"

    # 名称查询
    results = hierarchical_search(query)

    if not results:
        return "未找到对应的行政区划信息"
    elif len(results) == 1:
        return results[0][0]  # 单个结果直接返回代码
    else:
        # 多个结果用 | 分隔，代码和名称用 : 分隔
        return "|".join([f"{code}:{name}" for code, name in results])


def get_parent_division(code: str) -> Optional[Tuple[str, str]]:
    parent_code = get_parent_code(code)
    if parent_code and parent_code in DIVISION_DATA:
        return (parent_code, DIVISION_DATA[parent_code])
    return None