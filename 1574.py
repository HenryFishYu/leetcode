class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        length = len(arr)
        res = length
        l = 0
        r = length-1
        while r>0 and arr[r-1]<=arr[r]:
            r = r-1

        res = min(res,r)

        while l<r:
            while r<length and arr[r]<arr[l]:
                r = r+1
            res = min(res,r-l-1)

            if arr[l+1]<arr[l]:
                break

            l = l+1
        return res

Solution().findLengthOfShortestSubarray([1,2,3,10,0,7,8,9])