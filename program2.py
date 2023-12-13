def min_steps_to_empty(s):
    def is_palindrome(sub):
        return sub == sub[::-1]

    def find_largest_palindrome(start, end):
        largest_palindrome = ""
        for i in range(start, end + 1):
            for j in range(i, end + 1):
                if is_palindrome(s[i:j + 1]) and j - i + 1 > len(largest_palindrome):
                    largest_palindrome = s[i:j + 1]
        return largest_palindrome

    def min_steps_helper(start, end):
        if start >= end:
            return 0
        if memo[start][end] is not None:
            return memo[start][end]

        largest_palindrome = find_largest_palindrome(start, end)

        if largest_palindrome:
            memo[start][end] = 1 + min_steps_helper(start + len(largest_palindrome), end)
            return memo[start][end]

        min_steps = float('inf')
        for k in range(start, end):
            min_steps = min(min_steps, min_steps_helper(start, k) + min_steps_helper(k + 1, end))

        memo[start][end] = min_steps
        return min_steps

    n = len(s)
    memo = [[None] * n for _ in range(n)]
    return min_steps_helper(0, n - 1)

# Example usage:
input_str = input()
result = min_steps_to_empty(input_str)
print(f"Minimum steps to delete characters: {result}")