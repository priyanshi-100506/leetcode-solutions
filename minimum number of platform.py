class Solution:
    def findPlatform(self, Arrival, Departure):
        # Sort arrival and departure arrays
        arr = sorted([int(x) for x in Arrival])
        dep = sorted([int(x) for x in Departure])
        
        n = len(arr)
        platform_needed = 1
        max_platform = 1
        
        i = 1  # Pointer for arrivals
        j = 0  # Pointer for departures
        
        while i < n and j < n:
            # If the next train arrives before or at the same time the previous one departs
            if arr[i] <= dep[j]:
                platform_needed += 1
                i += 1
            # If the next train departs before the next one arrives
            else:
                platform_needed -= 1
                j += 1
                
            # Track the maximum platforms needed at any point
            max_platform = max(max_platform, platform_needed)
            
        return max_platform
