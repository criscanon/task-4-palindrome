def count_palindromes_enumeration(s):
    """
    Count the number of palindromes in a given string using enumeration method.
    
    Args:
    s (str): The input string
    
    Returns:
    int: Number of palindromes found in the input string
    """
    count = 0                       # O(1)
    n = len(s)                      # O(1)
    for i in range(n):              # O(n)
        for j in range(i+1, n+1):   # O(n)
            if s[i:j] == s[i:j][::-1]:  # O(j-i) ≈ O(n)
                count += 1          # O(1)
    return count                    # O(1)

# Complexity: O(n) * O(n) * O(n) ≈ O(n^3)