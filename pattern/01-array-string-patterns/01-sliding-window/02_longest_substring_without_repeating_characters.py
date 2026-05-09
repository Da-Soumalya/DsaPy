class Solution():
    def find_answer(self, s):
        seen, left, ans = set(), 0, 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            ans = max(ans, right-left+1)
        return ans


def main():
    s = "pwwkew"
    ob = Solution()
    ans = ob.find_answer(s)
    print(f"In the string {s}, the length of the longest substring without "
          f"repeating characters is: {ans}")


if __name__ == "__main__":
    main()