class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
      count = 0

      for num in range(low, high + 1):
        num_str = str(num)
        length = len(num_str)

        if length % 2 != 0:
            continue

        half = length // 2
        left_sum = 0
        right_sum = 0

        for i in range(half):
            left_sum += int(num_str[i])

        for i in range(half, length):
            right_sum += int(num_str[i])

        if left_sum == right_sum:
            count += 1
      return count

