n = int(input())
if n % 2 == 0:
    for col in range(1, int(n / 2) + 1):
        print("-" * int(n / 2 - col) + "*" + "-" * (col - 1) + "-" * (col - 1) + "*" + \
              "-" * int(n / 2 - col))
    for col in range(int(n / 2) - 1, 0, -1):
        print("-" * int(n / 2 - col) + "*" + "-" * (col - 1) + "-" * (col - 1) + "*" + \
              "-" * int(n / 2 - col))
    print()
else:
    for col in range(0, int(n / 2) + 1):
        if col == 0:
            print("-" * (int(n / 2) - col) + "*" + "-" * col + "-" * (col - 1) + "-" * (int(n / 2) - col))
        else:
            print("-" * (int(n / 2) - col) + "*" + "-" * col + "-" * (col - 1) + "*" + "-" * (int(n / 2) - col))
    for col in range(int(n / 2) - 1, -1, -1):
        if col == 0:
            print("-" * (int(n / 2) - col) + "*" + "-" * col + "-" * (col - 1) + "-" * (int(n / 2) - col))
        else:
            print("-" * (int(n / 2) - col) + "*" + "-" * col + "-" * (col - 1) + "*" + "-" * (int(n / 2) - col))
