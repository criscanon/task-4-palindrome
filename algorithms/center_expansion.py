def count_palindromes_center_expansion(s):
    """
    Count the number of palindromes in a given string using center expansion method.
    
    Args:
    s (str): The input string
    
    Returns:
    int: Number of palindromes found in the input string
    """
    count = 0                               # O(1)
    n = len(s)                              # O(1)
    for i in range(n):                      # O(n)
        # Expand around i as center (for odd-length palindromes)
        left = right = i                    # O(1)
        while left >= 0 and right < n and s[left] == s[right]:  # O(n)
            count += 1                      # O(1)
            left -= 1                       # O(1)
            right += 1                      # O(1)
        # Expand around i, i+1 as center (for even-length palindromes)
        left, right = i, i + 1              # O(1)
        while left >= 0 and right < n and s[left] == s[right]:  # O(n)
            count += 1                      # O(1)
            left -= 1                       # O(1)
            right += 1                      # O(1)
    return count                            # O(1)

# Complexity: O(n) * ( O(n) + O(n) ) ≈ O(n) * O(n) ≈ O(n^2)