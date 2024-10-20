class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k
    
def main():
    a=Solution()
    print(a.removeElement([0,1,2,3,4,5,3,2,3,3],3))

main()