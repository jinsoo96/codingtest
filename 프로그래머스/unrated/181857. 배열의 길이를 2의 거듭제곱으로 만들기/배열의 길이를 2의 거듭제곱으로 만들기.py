def solution(arr):
    length = len(arr)
    if length & (length - 1) == 0:  # Check if length is already a power of 2
        return arr
    else:
        power_of_two = 1
        while power_of_two < length:
            power_of_two *= 2
        num_zeros = power_of_two - length
        return arr + [0] * num_zeros
