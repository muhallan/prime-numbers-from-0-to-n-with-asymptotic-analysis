"""Prime numbers function."""

def prime_numbers(number):
    """Function to generate prime numbers from 0 to number."""
    prime_nums = []

    if not isinstance(number, int):
        return "Only integers are allowed."

    if number < 0:
        return "Negative numbers cannot be prime."

    if number in (0, 1):
        return "Zero or One cannot be prime numbers."

    for i in range(2, number + 1):
        if i > 1:
            for x in range(2, i):
                if (i % x) == 0:
                    break
            else:
                prime_nums.append(i)
    return prime_nums


"""
The asymptotic analysis of that algorithm is:
Using Big O notation; O(n^2/log n)
"""
