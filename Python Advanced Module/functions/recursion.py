def f1(index, n):
    if index == n:
        return

    print(index)
    f1(index + 1, max_index = max_index)

f1(index=0, max_index=n)