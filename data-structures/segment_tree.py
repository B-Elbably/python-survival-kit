"""
    Solve : 
    https://cses.fi/problemset/task/1648
    https://cses.fi/problemset/task/1649
    
    EDU: https://codeforces.com/edu/course/2/lesson/4
"""
import sys

sys.setrecursionlimit(200000)
input = lambda: sys.stdin.buffer.readline().decode().rstrip()

class Node:
    def __init__(self, v=0):
        self.val = v

class SegmentTree:
    def __init__(self, data: list[int]):
        self.skip = Node(0) # محايد للعملية
        
        N = len(data)
        self.size = 1
        while self.size < N:
            self.size <<= 1
        
        self.seg = [self.skip] * (self.size << 1)
        self._build(data, 0, 0, self.size - 1)

    def _merge(self, a: Node, b: Node) -> Node:
        return Node(a.val + b.val) # dont forget "skip"

    def _build(self, data: list[int], x: int, lx: int, rx: int):
        if lx == rx:
            if lx < len(data):
                self.seg[x] = Node(data[lx])
            return

        mid = (lx + rx) // 2
        left_child = (x << 1) + 1
        right_child = (x << 1) + 2
        
        self._build(data, left_child, lx, mid)
        self._build(data, right_child, mid + 1, rx)
        
        self.seg[x] = self._merge(self.seg[left_child], self.seg[right_child])

    def update(self, idx: int, value: int):
        self._update(0, 0, self.size - 1, idx, value)

    def _update(self, x: int, lx: int, rx: int, idx: int, value: int):
        if lx == rx:
            self.seg[x] = Node(value)
            return
        
        mid = (lx + rx) // 2
        left_child = (x << 1) + 1
        right_child = (x << 1) + 2
        
        if idx <= mid:
            self._update(left_child, lx, mid, idx, value)
        else:
            self._update(right_child, mid + 1, rx, idx, value)
            
        self.seg[x] = self._merge(self.seg[left_child], self.seg[right_child])

    def query(self, l: int, r: int) -> int:
        result_node = self._query(0, 0, self.size - 1, l, r)
        return int(result_node.val)

    def _query(self, x: int, lx: int, rx: int, l: int, r: int) -> Node:
        if lx > r or rx < l:
            return self.skip

        if l <= lx and rx <= r:
            return self.seg[x]

        mid = (lx + rx) // 2
        left_child = (x << 1) + 1
        right_child = (x << 1) + 2
        
        res_left = self._query(left_child, lx, mid, l, r)
        res_right = self._query(right_child, mid + 1, rx, l, r)
        
        return self._merge(res_left, res_right)


n, q = map(int, input().split())
v = list(map(int, input().split()))

sg = SegmentTree(v)

for _ in range(q):
    l, r = map(int, input().split())
    # Convert 1-based indices to 0-based for query: [l-1, r-1]
    print(sg.query(l - 1, r - 1))
