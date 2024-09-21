def sum(n: int) -> int:
    ret = 0
    for i in range(0, n + 1):
        ret = ret + i
    return ret


def sum_odd(n: int) -> int:
    ret = 0
    for i in range(1, n + 1, 2):
        ret = ret + i
    return ret


def sum_even(n: int) -> int:
    ret = 0
    for i in range(0, n + 1, 2):
        ret = ret + i
    return ret


def fib_recrusive(n: int) -> int:
    if n <= 2:
        return 1
    return fib_recrusive(n - 1) + fib_recrusive(n - 2)


def fib_iter(n: int) -> int:
    ret = 1
    tmp = 1
    for _ in range(n - 2):
        a = ret + tmp
        tmp = ret
        ret = a
    return ret
