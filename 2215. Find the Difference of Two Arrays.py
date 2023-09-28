class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        numeros1 = []
        numeros2 = []
        answer = []
        for n in nums1:
            if n not in nums2 and n not in numeros1:
                numeros1.append(n)
        for n in nums2:
            if n not in nums1 and n not in numeros2:
                numeros2.append(n)
        answer = (numeros1, numeros2)
        return answer