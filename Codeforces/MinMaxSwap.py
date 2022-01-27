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
        n = int(input())
        a = input().split(" ")
        a = list(map(int, a))
        b = input().split(" ")
        b = list(map(int, b))
        print(solve(a, b))
