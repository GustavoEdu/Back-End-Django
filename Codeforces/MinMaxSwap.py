def solve(a, b):
    for i in range(len(a)):
        if a[i] > b[i]:
            aux = a[i]
            a[i] = b[i]
            b[i] = aux
    return max(a) * max(b)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input()) # This variable doesn't affect the program already
        a = list(map(int, input().split(" ")))
        b = list(map(int, input().split(" ")))
        print(solve(a, b))
