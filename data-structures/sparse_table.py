import sys
input = lambda: sys.stdin.buffer.readline().decode().rstrip()
sys.setrecursionlimit(200000)
inf = float('inf')

class SparseTable:
    def __init__(self, data: list[int]):
        self.n = len(data)
        self.MAX_LOG = self.n.bit_length()
        
        # O(N) log_2 precomputation for O(1) query lookup
        self.log_table = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log_table[i] = self.log_table[i // 2] + 1
            
        # T[i][pw] stores the minimum in the range [i, i + 2^pw - 1]
        self.T = [[inf] * self.MAX_LOG for _ in range(self.n)]
        
        self._build(data)

    def _merge(self, a: int, b: int) -> int:
        return min(a, b) # (min , max, gcd, sum, etc.) but check code correctness for sum

    def _build(self, data: list[int]):
        for i in range(self.n):
            self.T[i][0] = data[i]
        
        for pw in range(1, self.MAX_LOG):
            step = (1 << (pw - 1))
            for i in range(self.n - (1 << pw) + 1):
                self.T[i][pw] = self._merge(self.T[i][pw - 1], self.T[i + step][pw - 1])

    # O(1) Range Minimum Query (RMQ)
    def query(self, l: int, r: int) -> int:
        if l > r or l < 0 or r >= self.n:
            return inf 

        k = self.log_table[r - l + 1]
        
        return self._merge(self.T[l][k], self.T[r - (1 << k) + 1][k])

# --- Execution Block ---

n, q = map(int, input().split())
s = list(map(int, input().split()))
st = SparseTable(s)
for _ in range(q):
    l, r = map(int, input().split())
    # Convert 1-based indices to 0-based for query: [l-1, r-1]
    print(st.query(l - 1, r - 1))
