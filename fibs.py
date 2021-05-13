"""Different ways to calculate Fibonacci numbers"""
import sys
import timeit
from functools import lru_cache
import decimal
sys.setrecursionlimit(5000)


@lru_cache()
def recursive_fib_cached(n):
    """recursive calculation with results cashing"""
    if n == 1 or n == 2:
        return 1

    return recursive_fib_cached(n - 1) + recursive_fib_cached(n - 2)


def iterative_fib(n):
    """iterative calculation"""
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a


def formula_fib_with_decimal(n):
    """using formula"""
    decimal.getcontext().prec = 300000

    root_5 = decimal.Decimal(5).sqrt()
    phi = ((1 + root_5) / 2)

    a = ((phi ** n) - ((-phi) ** -n)) / root_5

    return round(a)


def test_iterative_fib():
    assert iterative_fib(5) == 5, "iterative_fib: Ожидается значение, равное 5"


def test_recursive_fib_cached():
    assert recursive_fib_cached(5) == 5, "recursive_fib_cached: Ожидается значение, равное 5"


def test_formula_fib_with_decimal():
    assert formula_fib_with_decimal(5) == 5, "formula_fib_with_decimal: Ожидается значение, равное 5"


test_iterative_fib()
test_recursive_fib_cached()
test_formula_fib_with_decimal()

if __name__ == '__main__':
    print(iterative_fib(5))
    print(recursive_fib_cached(5))
    print(formula_fib_with_decimal(5))

    recu_f = 100000000000000000000000  # recursive_fib_cached(100_000)
    iter_f = iterative_fib(1_000_000)
    form_f = formula_fib_with_decimal(1_000_000)

    print(timeit.timeit('iterative_fib(1_000_000)',
                        setup='from __main__ import iterative_fib',
                        number=5))
    print(timeit.timeit('formula_fib_with_decimal(1_000_000)',
                        setup='from __main__ import formula_fib_with_decimal',
                        number=5))

    print(f"recu: {str(recu_f)[0:10]}...{str(recu_f)[-10:]}")
    print(f"iter: {str(iter_f)[0:10]}...{str(iter_f)[-10:]}")
    print(f"form: {str(form_f)[0:10]}...{str(form_f)[-10:]}")
