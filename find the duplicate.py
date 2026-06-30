class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # Phase 1: Find the intersection point of the two runners
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]          # Moves 1 step
            hare = nums[nums[hare]]            # Moves 2 steps
            if tortoise == hare:
                break
        # Phase 2: Find the entrance to the cycle (the duplicate number)
        tortoise = nums[0]                     # Reset tortoise to start
        while tortoise != hare:
            tortoise = nums[tortoise]          # Moves 1 step
            hare = nums[hare]                  # Moves 1 step
        return tortoise
