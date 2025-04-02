class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
       r = m+n-1
       m1=m-1
       n1=n-1
       while n1 >= 0:
           if m1 >= 0 and nums1[m1]>nums2[n1]:
             nums1[r]=nums1[m1]
             m1-=1
           else:
             nums1[r]=nums2[n1]
             n1-=1
           r-=1        
