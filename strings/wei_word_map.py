class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = []
        for word in words:
            total = sum(weights[ord(char) - ord('a')] for char in word)
            rem = total % 26
            mapped = chr(ord('z') - rem)
            res.append(mapped)
        return "".join(res)
