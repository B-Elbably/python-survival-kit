import sys
from bisect import bisect_right

input = lambda: sys.stdin.buffer.readline().decode().rstrip()
sys.setrecursionlimit(200000)

class MergeSortTree:
    def __init__(self, data: list[int]):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        
        self.seg = [[] for _ in range(self.size << 1)]
        self._build(data, 0, 0, self.size - 1)

    def _merge(self, left_list: list[int], right_list: list[int]) -> list[int]:
        merged = []
        i, j = 0, 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] <= right_list[j]:
                merged.append(left_list[i])
                i += 1
            else:
                merged.append(right_list[j])
                j += 1
        merged.extend(left_list[i:])
        merged.extend(right_list[j:])
        return merged

    def _build(self, data: list[int], x: int, lx: int, rx: int):
        if lx == rx:
            if lx < self.n:
                self.seg[x] = [data[lx]]
            return

        mid = (lx + rx) >> 1
        left_child = (x << 1) + 1
        right_child = (x << 1) + 2
        
        self._build(data, left_child, lx, mid)
        self._build(data, right_child, mid + 1, rx)
        
        self.seg[x] = self._merge(self.seg[left_child], self.seg[right_child])

    def query(self, l: int, r: int, k: int) -> int:
        return self._query(0, 0, self.size - 1, l, r, k)

    def _query(self, x: int, lx: int, rx: int, l: int, r: int, k: int) -> int:
        if lx > r or rx < l:
            return 0

        if l <= lx and rx <= r:
            return bisect_right(self.seg[x], k)

        mid = (lx + rx) >> 1
        left_child = (x << 1) + 1
        right_child = (x << 1) + 2
        
        res_left = self._query(left_child, lx, mid, l, r, k)
        res_right = self._query(right_child, mid + 1, rx, l, r, k)
        
        return res_left + res_right

# --- Execution Block ---
n , q = map(int, input().split())
s = list(map(int, input().split()))

tree = MergeSortTree(s)

for _ in range(q):
    # Query: count of numbers <=k in range [l, r]
    l, r , k = map(int, input().split())
    print(tree.query(l - 1, r - 1, k))
