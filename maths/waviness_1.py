class Solution:

  def totalWaviness(self, num1: int, num2: int) -> int:
    ans = 0
    for x in range(num1, num2 + 1):
      ans += self.getWaviness(x)
    return ans

  def getWaviness(self, num: int) -> int:
    s = str(num)
    if len(s) < 3:
      return 0
    count = 0
    for i in range(1, len(s) - 1):
      if (s[i] > s[i - 1] and s[i] > s[i + 1]) or (
          s[i] < s[i - 1] and s[i] < s[i + 1]
      ):
        count += 1
    return count
