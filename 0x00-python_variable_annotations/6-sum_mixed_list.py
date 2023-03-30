#usr/bin/env python3
"""A type-annotation of sum_mixed_list."""
from typing import List, Union
"""Type annoted mixed function"""
def sum_mixed_list(mxd_lst:List[Union[int,float]]) -> float:
    """Return sum of lists."""
    return float (sum(mxd_lst))
