class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        pivot = 0
        
        # 1. Find the pivot (using break instead of return)
        for i in range(N - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                pivot = i
                break
        
        # 2. Edge case: if entirely decreasing, sort and exit
        if pivot == 0:
            nums.sort()
            return

        # 3. Find the number which needs to be swapped (Fix indentation)
        swap = N - 1
        while nums[pivot - 1] >= nums[swap]:
            swap -= 1
            
        # 4. Swap
        nums[swap], nums[pivot - 1] = nums[pivot - 1], nums[swap]
        
        # 5. Reverse/Sort the suffix
        nums[pivot:] = sorted(nums[pivot:])
