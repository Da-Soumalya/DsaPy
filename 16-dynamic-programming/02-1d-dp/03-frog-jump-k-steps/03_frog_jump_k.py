'''
Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the 
(N-1)th stair. At a time the frog can climb either one or two steps. 
A height[N] array is also given. Whenever the frog jumps from a stair i to stair j, 
the energy consumed in the jump is abs(height[i]- height[j]), where abs() means the 
absolute difference. We need to return the minimum energy that can be used by the 
frog to jump from stair 0 to stair N-1.
'''


class Solution:
    def solve_util(self, ind, height, dp, k):
        if ind == 0:
            return 0
        if dp[ind] != -1: # escaping the overlapping subproblems
            return dp[ind]

        min_step = float('inf') # cases where k step jumps could go to -ve index

        for j in range(1, k+1):
            if not ind - j < 0:
                jump = self.solve_util(ind-j, height, dp, k) + abs(height[ind] - height[ind-j])
                min_step = min(jump, min_step)
        dp[ind] = min_step
        return dp[ind]

    def frog_jump(self, height, k):
        if not height: # if the height array was empty
            return 0
        
        n = len(height)
        dp = [-1]*n

        return self.solve_util(ind=n-1, height=height, dp=dp, k=k) # top-down. Traversing from Nth to 0th index
        ''' difference in argument order brings different result, which is why we used 
        keyword arguments here. '''


def main():
    # Not taking an user input
    height = [30, 10, 60, 10, 60, 50] # answer is 40.
    k = 2

    sol = Solution()
    answer = sol.frog_jump(height, k)
    
    print(f"The height array: {height}\n"
          f"Total possible jumps in a turn: {k}\n"
          f"The minimum energy needed to traverse it is: {answer}")  # Expected: 40


if __name__ == "__main__":
    main() 