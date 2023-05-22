def solution(arr):
    prev_arr = arr[:]
    x = 0
    while True:
        next_arr = [n//2 if n >= 50 and n%2==0 else 2*n+1 if n < 50 and n%2==1 else n for n in prev_arr]
        if next_arr == prev_arr:
            break
        prev_arr = next_arr[:]
        x += 1
    return x