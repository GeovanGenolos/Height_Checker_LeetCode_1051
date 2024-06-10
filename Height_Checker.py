from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Step 1: Create the expected sorted array
        expected = sorted(heights)
        
        # Step 2: Compare heights with expected and count mismatches
        mismatch_count = sum(heights[i] != expected[i] for i in range(len(heights)))
        
        return mismatch_count

if __name__ == "__main__":
    solution = Solution()
    
    heights1 = [1, 1, 4, 2, 1, 3]
    heights2 = [5, 1, 2, 3, 4]
    heights3 = [1, 2, 3, 4, 5]