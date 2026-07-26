class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        if len(nums1) > len(nums2):
            A = nums2
            B = nums1
        total = len(nums1) + len(nums2)
        half = total // 2
        left = 0
        right = len(A) - 1
        while True:
            mid = (left + right) // 2
            other = half - mid - 2
            ALeft = A[mid] if mid >= 0 else float('-inf')
            ARight = A[mid + 1] if (mid + 1) < len(A) else float('inf')
            BLeft = B[other] if other >= 0 else float('-inf')
            BRight = B[other + 1] if (other + 1) < len(B) else float('inf')

            if ALeft <= BRight and BLeft <= ARight:
                if total % 2 == 0:
                    return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
                else:
                    return min(ARight, BRight)
            elif ALeft > BRight:
                right = mid - 1
            else:
                left = mid + 1
