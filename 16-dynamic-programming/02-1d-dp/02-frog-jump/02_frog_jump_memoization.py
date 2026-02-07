'''
Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the 
(N-1)th stair. At a time the frog can climb either one or two steps. 
A height[N] array is also given. Whenever the frog jumps from a stair i to stair j, 
the energy consumed in the jump is abs(height[i]- height[j]), where abs() means the 
absolute difference. We need to return the minimum energy that can be used by the 
frog to jump from stair 0 to stair N-1.
'''


class Solution:
    def solve(self, ind, height, dp):
        if ind == 0:
            return 0
        if dp[ind] != -1: # escaping the overlapping subproblems
            return dp[ind]

        jump_two = float('inf') # useful when ind == 1

        jump_one = self.solve(ind-1, height, dp) + abs(height[ind]-height[ind-1])
        if ind > 1:
            jump_two = self.solve(ind-2, height, dp) + abs(height[ind]-height[ind-2])
        dp[ind] = min(jump_one, jump_two) # denotes the total energy expended by the frog
        return dp[ind]

    def frog_jump(self, height):
        if not height: # if the height array was empty
            return 0
        
        n = len(height)
        dp = [-1]*n

        return self.solve(ind=n-1, dp=dp, height=height) # top-down. Traversing from Nth to 0th index
        ''' difference in argument order brings different result, which is why we used 
        keyword arguments here. '''


def main():
    # Not taking an user input
    height = [30, 10, 60, 10, 60, 50] # answer is 40.

    sol = Solution()
    answer = sol.frog_jump(height)
    
    print(f"The height array: {height}\n"
          f"The minimum energy needed to traverse it is: {answer}")  # Expected: 40


if __name__ == "__main__":
    main() 