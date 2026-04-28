from collections import defaultdict
import math

class Solution:
    def gcdSort(self, nums: list[int]) -> bool:
        n = len(nums)

        # DSU (Union-Find)
        parent = {}
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent.setdefault(x, x)
            parent.setdefault(y, y)
            parent[find(x)] = find(y)

        # Factorize each number and union with its prime factors
        def primeFactors(x):
            factors = []
            d = 2
            while d * d <= x:
                if x % d == 0:
                    factors.append(d)
                    while x % d == 0:
                        x //= d
                d += 1
            if x > 1:
                factors.append(x)
            return factors

        for num in nums:
            factors = primeFactors(num)
            for f in factors:
                union(num, f)

        # Check if nums can be rearranged to sorted order
        sorted_nums = sorted(nums)
        for a, b in zip(nums, sorted_nums):
            if find(a) != find(b):
                return False
        return True
