def sequencia(n, memo=None):

    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 3:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
    memo[n] = (
        sequencia(n - 1)
        + 2 * sequencia(n - 2)
        + 3 * sequencia(n - 3)
        )
    return memo[n]

def main():
    n = int(input())
    print(sequencia(n))

main()