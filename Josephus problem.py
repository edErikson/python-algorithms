def josephus(n, k):
    m = list(range(1, n + 1))
    ans = []
    i = 0

    while m:
        i = (i + k - 1) % len(m)
        ans.append(m.pop(i))

    return ans


print(josephus(23, 6))


def josephus2(n, k):
    if n == 1:
        return 1
    return (josephus(n - 1, k) + k - 1) % n + 1


# Example:
n = 23  # Number of individuals
k = 6  # Elimination interval
print("Last survivor's position:", josephus(n, k))