class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        # grid represents the awareness of people
        grid = [0] * forget
        grid[-1] = 1  
        res = 1  
        count = 0  
        
        for _ in range(1, n):
            # Remove the earliest person's awareness from the front of the grid
            temp = grid.pop(0)
            
            # Update the result and count variables
            res = res - temp
            count = count - temp
            count += grid[-delay]  # Add the awareness of the person at index 'delay' from the end
        
            grid.append(count)

            res += count

        return res % (10**9 + 7)
