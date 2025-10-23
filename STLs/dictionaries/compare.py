"""
Memory Usage Comparison
"""

from collections import defaultdict, OrderedDict
import sys

regular_dict = {i: i for i in range(1000)}
default_dict = defaultdict(int, {i: i for i in range(1000)})
ordered_dict = OrderedDict({i: i for i in range(1000)})

print("Memory usage:")
print(f"Regular dict: {sys.getsizeof(regular_dict)} bytes")
print(f"DefaultDict:  {sys.getsizeof(default_dict)} bytes")
print(f"OrderedDict:  {sys.getsizeof(ordered_dict)} bytes")


"""
                    dict	   defaultdict	        OrderedDict

Memory Usage	    Lowest	    Low	                 Higher
Performance	        Fastest	    Fast	             Slower
Use Case	        General     purpose	Grouping	 LRU cache,
                                ,counting            ordered config
"""
