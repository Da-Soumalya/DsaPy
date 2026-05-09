'''
A ninja has planned a n-day training schedule. Each day he has to perform one of three 
activities - running, stealth training, or fighting practice. The same activity cannot 
be done on two consecutive days and the ninja earns a specific number of merit points, 
based on the activity and the given day.


Given a n x 3-sized matrix, where matrix[i][0], matrix[i][1], and matrix[i][2], represent 
the merit points associated with running, stealth and fighting practice, on the 
(i+1)th day respectively. Return the maximum possible merit points that the ninja can earn.
'''


class Solution:
    def helper(self, merit_arr, last_task, dp, day):
        # if already calculated, use the overlapping subproblem
        if dp[day][last_task] != -1:
            return dp[day][last_task] 

        # base case: first case
        if day == 0:
            max_merit = 0
            for i in range(3):
                if i != last_task:
                    max_merit = max(max_merit, merit_arr[0][i])
            dp[day][last_task] = max_merit
            return max_merit
        
        max_merit = 0
        for i in range(3):
            if i != last_task:
                activity = merit_arr[day][i] + self.helper(merit_arr, i, dp, day-1)
                max_merit = max(max_merit, activity)
        dp[day][last_task] = max_merit
        return max_merit

    def ninja_training(self, merit_arr, n):
        dp = [[-1 for _ in range(4)] for _ in range(n)]
        return self.helper(merit_arr, 3, dp, n-1)


def main():
    merit_arr = [
        [10, 40, 70],
        [20, 50, 80],
        [30, 60, 90],
    ]
    total_days = len(merit_arr)
    ob = Solution()
    answer = ob.ninja_training(merit_arr, total_days) # to compute the max merit
    print(answer)


if __name__ == "__main__":
    main()