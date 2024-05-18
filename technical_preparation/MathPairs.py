def pairs(k, arr):
    count = 0
    # arr.append(arr[0])
    for i in range(len(arr)):
        # print(i,arr[arr.index(i):])
        # print(arr[i],arr[i+1:])
        # other_arr = arr[arr.index(i):]
        # for j in arr[arr.index(i):]:
        if i == (len(arr) - 1):
            break
        else:
            for j in range(i, len(arr)):
                if abs(arr[i] - arr[j]) == k:
                    # print(arr[i],arr[j])
                    # print(abs(arr[i]-arr[j]))
                    count += 1

    return count


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    # fptr.write(str(result) + "\n")
