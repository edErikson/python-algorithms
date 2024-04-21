def josephus(n, k):
    m = list(range(1, n + 1))
    ans = []
    i = 0

    while m:
        i = (i + k - 1) % len(m)
        ans.append(m.pop(i))

    return ans


print(josephus(23, 6))
