class Solution:
    def two_sum(self,nums,target):
        tudien={}

        for i,num in enumerate(nums):
            complement=target-num
            if complement in tudien:
                return [i,tudien[complement]]
            tudien[num]=i
        return []
a=Solution()
print(a.two_sum([2,7,11,15],9))