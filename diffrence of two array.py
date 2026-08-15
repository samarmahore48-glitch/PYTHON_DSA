class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums3=set(nums1)
        nums4=set(nums2)
        answer=[list(nums3-nums4),list(nums4-nums3)]
        return answer


        