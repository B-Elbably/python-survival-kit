"""
    solve :
    https://cses.fi/problemset/task/1735
"""

import sys

sys.setrecursionlimit(200000)
input = lambda: sys.stdin.buffer.readline().decode().rstrip()

class Node:
    # Initialize val for RSQ (Sum) and lazy for Range Add
    def __init__(self, v=0, l=0):
        self.val = v
        self.lazy = l

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

    # Apply lazy value v to node x, which covers range [lx, rx]
    def _apply(self, x: int, lx: int, rx: int, v: int):
        range_length = rx - lx + 1
        self.seg[x].val += v * range_length 
        self.seg[x].lazy += v 

    def _push(self, x: int, lx: int, rx: int):
        if self.seg[x].lazy == 0:
            return
        
        if lx != rx:
            mid = (lx + rx) // 2
            left_child = (x << 1) + 1
            right_child = (x << 1) + 2
            
            self._apply(left_child, lx, mid, self.seg[x].lazy)
            self._apply(right_child, mid + 1, rx, self.seg[x].lazy)
            
        self.seg[x].lazy = 0

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

    def update(self, l: int, r: int, val: int):
        self._update(0, 0, self.size - 1, l, r, val)

    def _update(self, x: int, lx: int, rx: int, l: int, r: int, val: int):
        if lx > r or rx < l: # Out of range
            return
        if l <= lx and rx <= r:
            self._apply(x, lx, rx, val)
            return
        
        self._push(x, lx, rx) # Push lazy
        
        mid = (lx + rx) // 2
        left_child = (x << 1) + 1
        right_child = (x << 1) + 2
        
        self._update(left_child, lx, mid, l, r, val)
        self._update(right_child, mid + 1, rx, l, r, val)
            
        self.seg[x] = self._merge(self.seg[left_child], self.seg[right_child])

    def query(self, l: int, r: int) -> int:
        result_node = self._query(0, 0, self.size - 1, l, r)
        return int(result_node.val)

    def _query(self, x: int, lx: int, rx: int, l: int, r: int) -> Node:
        if lx > r or rx < l:
            return self.skip

        if l <= lx and rx <= r:
            return self.seg[x]
        
        self._push(x, lx, rx) 
        
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
    query = list(map(int, input().split()))
    op = query[0]

    if op == 1:
        l, r, val = query[1], query[2], query[3]
        sg.update(l - 1, r - 1, val)
    elif op == 2:
        # 1-based indices [l, r] become 0-based [l-1, r-1]
        l, r = query[1], query[2]
        print(sg.query(l - 1, r - 1))

