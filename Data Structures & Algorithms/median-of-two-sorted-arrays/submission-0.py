class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        small, big = nums1, nums2
        if m > n:
            m, n = n, m
            small, big = big, small
        half = math.floor((m + n) / 2) 

        small = [float('-inf')] + small + [float("inf")]
        big = [float('-inf')] + big + [float("inf")]
        l = 1
        r = m
        while l <= r:
            smallr = l + int((r-l)/2)
            bigr = half - smallr
            if small[smallr] > big[bigr + 1]:
                r = smallr - 1
            elif big[bigr] > small[smallr + 1]:
                l = smallr + 1
            else:
                if (n + m) % 2 == 0:
                    return (max(small[smallr],big[bigr]) + min(small[smallr+1],big[bigr+1])) / 2
                else:
                    return min(small[smallr+1], big[bigr+1])
        smallr = r
        bigr = half - smallr
        if (n + m) % 2 == 0:
            return (max(small[smallr],big[bigr]) + min(small[smallr+1],big[bigr+1])) / 2
        else:
            return min(small[smallr+1], big[bigr+1])

 

