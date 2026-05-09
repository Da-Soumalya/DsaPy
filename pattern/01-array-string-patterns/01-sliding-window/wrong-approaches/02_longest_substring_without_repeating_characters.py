class Solution():
    def find_answer(self, s):
        l = len(s)
        ans, temp_str = s[0], s[0]
        left, right = 0, 0
        for i in range(1, l):
            flag = 0
            for j in range(left, right+1):
                if s[j] == s[i]:
                    left = i
                    right = i
                    temp_str = s[left:right+1]
                    flag = 1
                    break
            if flag == 1:
                continue
            temp_str += s[i]
            right += 1
            if len(temp_str) > len(ans):
                ans = temp_str
        return ans


def main():
    s = "pwwkew"
    ob = Solution()
    ans = ob.find_answer(s)
    print(f"In the string {s}, the longest substring without "
          f"repeating characters is: {ans}")


if __name__ == "__main__":
    main()