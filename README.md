<div align="center">

# python-survival-kit

**Python reference implementations of algorithms and data structures for competitive programming.**

![Python 3](https://img.shields.io/badge/Python-3-3776AB?style=flat-square&logo=python&logoColor=white)
![Competitive programming](https://img.shields.io/badge/Competitive-Programming-0969DA?style=flat-square)

</div>

## Why

During a contest there is no time to rederive Dijkstra or a segment tree. This repo keeps short, readable, contest-ready Python versions of the classics, each in its own file, so you can find one quickly and copy it.

## What's inside

- Graph algorithms: BFS/DFS, shortest paths, MST with DSU, cycle detection, topological sort
- Data structures: Fenwick trees (1D and 2D), segment trees (plain and lazy), sparse table, LCA
- Dynamic programming classics: LCS, LIS, knapsack and more
- Number theory and combinatorics: sieve, modular inverse, matrix exponentiation, binomials, Catalan numbers
- Python equivalents of C++ STL containers, plus a fast-input contest template

## Quick start

```bash
git clone https://github.com/B-Elbably/python-survival-kit.git
cd python-survival-kit
python3 stls/deque.py
```

Each file is standalone and needs only the Python standard library.

## Usage

Container and utility files print a small demo when run. Problem-style files read from standard input, like a contest solution. For example, Dijkstra reads `n m`, then `m` weighted edges, and finds the shortest path from node 1 to node `n`:

```bash
printf '3 3\n1 2 5\n2 3 4\n1 3 20\n' | python3 graph/shortest-path/dijkstra.py
# Distance: 9
# Path: 1 2 3
```

To use a snippet in a contest, copy the file contents and keep the fast-input lines from `template.py`.

## Project structure

| Folder | Contents |
| --- | --- |
| `counting/` | Combinatorics: binomials, Catalan numbers, derangements, permutations, stars and bars, inclusion-exclusion |
| `data-structures/` | BIT (1D/2D), segment trees (plain and lazy), merge-sort tree, sparse table, LCA |
| `dp/` | LCS, LIS, knapsack, minimizing coins, minimum path sum and other classics |
| `graph/` | Traversal (BFS/DFS, topological sort, tree diameter), shortest paths, MST/DSU, cycle detection |
| `maths/` | Fast power, sieve, SPF, totient, modular inverse, matrix exponentiation |
| `searching-algorithms/` | Linear, binary, ternary, jump and Fibonacci search |
| `sorting-algorithms/` | Bubble, selection, insertion, merge, quick, counting |
| `static-range-queries/` | Prefix sums and partial sums in 1D and 2D |
| `stls/` | Python equivalents of C++ STL containers: deque, queues, stack, sets, dictionaries |
| `modules/` | Useful standard-library modules: `collections`, `heapq`, `itertools`, plus `tricks/` |
| `misc/` | Backtracking (N-Queens), balanced brackets, expression parsing, Huffman coding |
| `template.py` | Starter template for contest solutions |

Folder names are lowercase; multi-word folders use hyphens and file names use underscores.

## Contact

Maintained by [Belal Elbably](https://github.com/B-Elbably) · [LinkedIn](https://linkedin.com/in/elbably) · [Codeforces](https://codeforces.com/profile/Belal.echo)
