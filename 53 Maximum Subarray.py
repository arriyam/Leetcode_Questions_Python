class Solution:
    def maxSubArray(self, a: List[int]) -> int:
        mst = 0
        meh = 0
        for i in range(len(a)):
            meh = meh + a[i]
            if meh < a[i]:
                meh = a[i]
            if mst < meh:
                mst = meh

        if mst == 0:
            return max(a)
        else:
            return mst