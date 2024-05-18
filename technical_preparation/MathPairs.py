# Find the pairs of numbers that can give a certain result with their sum. Given an array of numbers and a k result.

def pairs(k, arr):
    count = 0

    for i in range(len(arr)):
        if i == (len(arr) - 1):
            break
        else:
            for j in range(i, len(arr)):
                if abs(arr[i] - arr[j]) == k:
                    count += 1

    return count


if __name__ == "__main__":

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)
