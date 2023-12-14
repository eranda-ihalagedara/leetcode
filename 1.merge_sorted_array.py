class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1, idx2 = 0, 0
        
        while idx2 < n:
            if idx1 >= m:
                # Add nums2[idx2:] to nums1[idx1:] and break
                nums1[idx1:] = nums2[idx2:]
                break
            
            elif nums1[idx1] > nums2[idx2]:
                # Shift nums1[idx1:m] to right and 
                # insert nums2[idx2] in vacant place and
                # m++, idx2++
                nums1[idx1+1:] = nums1[idx1:-1]
                nums1[idx1] = nums2[idx2]
                
                m += 1
                idx2 += 1
            
            idx1 += 1

        
    def merge_optimized(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n > 0:
            if m > 0 and nums1[m-1]>nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m-=1
            else:
                nums1[m+n-1] = nums2[n-1]
                n-=1

                