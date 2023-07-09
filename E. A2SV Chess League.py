from sys import stdin, stdout

# Reading input values from standard input
n, k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

# Function to recursively solve the problem
def solve(i, count, k):
    # Base case, when only one element is left in a sub-array
    if count == 1:
        return [i]

    # Divide the sub-array into two halves and solve each recursively
    left = solve(i, count // 2, k)
    right = solve(i + (count // 2), count // 2, k)

    # Merge the two sorted halves while checking the difference between elements
    merged = []
    l_ptr = r_ptr = 0
    left_min, right_min = arr[left[0]], arr[right[0]]

    while l_ptr < len(left) and r_ptr < len(right):
        if arr[left[l_ptr]] <= arr[right[r_ptr]]:
            if right_min - arr[left[l_ptr]] <= k:
                merged.append(left[l_ptr])
            l_ptr += 1
        else:
            if left_min - arr[right[r_ptr]] <= k:
                merged.append(right[r_ptr])
            r_ptr += 1

    # Add any remaining elements from left or right halves while checking the difference between elements
    while l_ptr < len(left) and right_min - arr[left[l_ptr]] <= k:
        merged.append(left[l_ptr])
        l_ptr += 1

    while r_ptr < len(right) and left_min - arr[right[r_ptr]] <= k:
        merged.append(right[r_ptr])
        r_ptr += 1

    # Return the merged and sorted sub-array
    return merged


# Print the sorted and transformed sub-array obtained by calling the solve() function
print(*sorted(map(lambda x: x + 1, solve(0, 2**n, k))))
