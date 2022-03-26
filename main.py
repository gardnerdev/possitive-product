# Python3 program to implement
# the above approach

# Function to find the length of
# longest subarray whose product
# is 1
def maxLenSub(arr, N):

    # Stores the length of current
    # subarray with positive product
    Pos = 0

    # Stores the length of current
    # subarray with negative product
    Neg = 0

    # Stores the length of the longest
    # subarray with positive product
    res = 0

    for i in range(N):
        if arr[i] == 0:

            # Reset the value
            Pos = Neg = 0

        # If current element is 1
        elif arr[i] == 1:

            # Increment the length of
            # subarray with positive product
            Pos += 1

            # If at least one element is
            # present in the subarray with
            # negative product
            if Neg != 0:
                Neg += 1

            # Update res
            res = max(res, Pos)

        # If current element is negative
        elif arr[i] == -1:
            Pos, Neg = Neg, Pos

            # Increment the length of subarray
            # with negative product
            Neg += 1

            # If at least one element is present
            # in the subarray with positive product
            if Pos != 0:
                Pos += 1

            # Update res
            res = max(res, Pos)

    return res


# Driver Code
if __name__ == "__main__":

    arr = [1, -1, -1, 1, 1, -1]
    N = len(arr)
    print(maxLenSub(arr, N))

    arr = [1, -1, -1, -1, 1, 1]
    N = len(arr)
    print(maxLenSub(arr, N))
