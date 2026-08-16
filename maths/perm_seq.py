'''
strategy to be used here:
    - factorial numbering system

complexity:
    - O(n^2) time and O(n) space
'''

class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        # precompute factorials
        factorials = [1] * n
        for i in range(1, n):
            factorials[i] = factorials[i-1] * i

        # convert to zero index
        k -= 1

        # avail nums to select from
        numbers = list(range(1, n+1))
        results = []

        for i in range(n):
            fact = factorials[n - 1 - i]
            idx = k // fact
            results.append(str(numbers[idx]))
            numbers.pop(idx)

            k %= fact

        return ''.join(results)