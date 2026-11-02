"""
    Huffman Coding Implementation in Python (AI-Generated)
"""

import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    if not text:
        return None
    
    freq = defaultdict(int)
    for char in text:
        freq[char] += 1
    
    heap = []
    for char, count in freq.items():
        heapq.heappush(heap, Node(char, count))
    
    # Build Huffman tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    return heapq.heappop(heap)

def generate_codes(root):
    codes = {}
    
    def traverse(node, code):
        if node:
            if node.char is not None:  # Leaf node
                codes[node.char] = code
            traverse(node.left, code + '0')
            traverse(node.right, code + '1')
    
    traverse(root, "")
    return codes

def huffman_encode(text):
    if not text:
        return "", {}
    
    root = build_huffman_tree(text)
    codes = generate_codes(root)
    
    encoded = ''.join(codes[char] for char in text)
    return encoded, codes

def huffman_decode(encoded, root):
    if not encoded:
        return ""
    
    decoded = []
    node = root
    
    for bit in encoded:
        if bit == '0':
            node = node.left
        else:
            node = node.right
        
        if node.char is not None:  # Reached leaf node
            decoded.append(node.char)
            node = root  # Reset to root for next character
    
    return ''.join(decoded)

# Example usage:
text = "hello world"
encoded, codes = huffman_encode(text)
print(f"Original: {text}")
print(f"Encoded: {encoded}")
print("Huffman Codes:")
for char, code in codes.items():
    print(f"  {repr(char)}: {code}")

# Decoding (need to rebuild tree for demonstration)
root = build_huffman_tree(text)
decoded = huffman_decode(encoded, root)
print(f"Decoded: {decoded}")