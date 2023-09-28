class Solution:
    def arraySign(self, nums: List[int]) -> int:
        produto = 1
        for n in nums:
            produto *= n
        if produto > 0:
            return 1
        elif produto < 0:
            return -1
        else:
            return 0