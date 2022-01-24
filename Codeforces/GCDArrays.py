if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        data = input()
        arr = list(map(int, data.split(" ")))
        l, r, k = arr[0], arr[1], arr[2]
        if l == r:
            if l == 1:
                print("NO")
            else:
                print("YES")
        else:
            length = r - l + 1
            if length % 2 == 0:
                if length // 2 <= k:
                    print("YES")
                else:
                    print("NO")
            else:
                if l % 2 == 0:
                    if length // 2 <= k:
                        print("YES")
                    else:
                        print("NO")
                else:
                    if length // 2  + 1 <= k:
                        print("YES")
                    else:
                        print("NO")
