'''
strategy to be used here:
    - brute force

complexity:
    - O(n^2) time and O(1) space
'''

class Solution:
    def numTeams(self, rating: list[int]) -> int:
        total_teams = 0
        n = len(rating)
      
        # For each soldier at position i, consider it as the middle soldier
        for i in range(n):
            current_rating = rating[i]
          
            # Count soldiers to the left with smaller rating
            smaller_left = sum(1 for left_rating in rating[:i] if left_rating < current_rating)
          
            # Count soldiers to the right with greater rating
            greater_right = sum(1 for right_rating in rating[i + 1:] if right_rating > current_rating)
          
            # Ascending teams: left < current < right
            total_teams += smaller_left * greater_right
          
            # Calculate soldiers to the left with greater rating
            greater_left = i - smaller_left
          
            # Calculate soldiers to the right with smaller rating
            smaller_right = (n - i - 1) - greater_right
          
            # Descending teams: left > current > right
            total_teams += greater_left * smaller_right
      
        return total_teams