class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def isBalanced(x: int) -> bool:
            from collections import Counter
            freq = Counter(str(x))
            for d, count in freq.items():
                if int(d) != count:
                    return False
            return True

        num = n + 1
        while True:
            if isBalanced(num):
                return num
            num += 1
