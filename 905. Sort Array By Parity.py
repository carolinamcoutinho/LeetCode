class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        numeros = 0
        even = []
        odd = []
        for n in nums:
            if n % 2 == 0:
                even.append(n)
            else:
                odd.append(n)
        numeros = even + odd
        return numeros