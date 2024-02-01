class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Initialize search space
        left, right = 1, max(piles)
        ans = right

        # Binary search
        while left <= right:
            # Calculate the middle value
            mid = (left + right) // 2
            hours = 0

            # Calculate total hours required to eat all bananas at the current speed
            for bananas in piles:
                hours += math.ceil(bananas / mid)

            # Update answer if the current speed allows all bananas to be eaten within h hours
            if hours <= h:
                ans = min(ans, mid)
                # Explore lower eating speeds
                right = mid - 1
            else:
                # Explore higher eating speeds
                left = mid + 1

        return ans    