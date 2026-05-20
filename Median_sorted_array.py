class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # always binary search smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x = len(nums1)
        y = len(nums2)

        low = 0
        high = x

        while low <= high:

            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            leftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            rightX = float('inf') if partitionX == x else nums1[partitionX]

            leftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            rightY = float('inf') if partitionY == y else nums2[partitionY]

            # correct partition found
            if leftX <= rightY and leftY <= rightX:

                # odd length
                if (x + y) % 2 == 1:
                    return max(leftX, leftY)

                # even length
                return (
                    max(leftX, leftY) +
                    min(rightX, rightY)
                ) / 2

            # move left
            elif leftX > rightY:
                high = partitionX - 1

            # move right
            else:
                low = partitionX + 1
        