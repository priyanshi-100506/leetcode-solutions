from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort intervals by their start times
        intervals.sort(key=lambda x: x[0])
        
        # Initialize the result list with the first interval
        merged = [intervals[0]]
        
        # Step 2: Iterate through the remaining intervals
        for current in intervals[1:]:
            prev_start, prev_end = merged[-1]
            curr_start, curr_end = current
            
            # If the current interval overlaps with the previous one
            if curr_start <= prev_end:
                # Merge them by updating the end time of the previous interval
                merged[-1][1] = max(prev_end, curr_end)
            else:
                # No overlap, so safely add the current interval to the result
                merged.append(current)
                
        return merged
