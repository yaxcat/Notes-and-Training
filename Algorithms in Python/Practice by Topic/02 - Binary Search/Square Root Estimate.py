def square_root(n: int) -> int:
    if n < 0:
        return 0
    s = 0
    r = n//2
    e = n
    while s <= e:
        if r*r > n:
            if r*r-n < 1:
                return int(r)
            else:
                e = r-1
        else:
            s = r+1
        r = (s+e)//2
    return r

if __name__ == "__main__":
    n = int(input())
    res = square_root(n)
    print(res)
