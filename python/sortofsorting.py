from random import randrange


# using randomized quicksort (does not work)
def r_qs(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        # pick random pivot and move to front
        pivot_index = randrange(low, high+1)
        arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
        # reference value to compare against the rest of the array
        pivot_val = arr[low]

        # partition
        swap_index = low + 1
        for j in range(low+1, high+1):
            # compare first 2 chars, then full string for stability
            if arr[j][:2] < pivot_val[:2]:
                arr[swap_index], arr[j] = arr[j], arr[swap_index]
                swap_index += 1

        # place pivot into its final place; pivot is considered sorted
        arr[low], arr[swap_index-1] = arr[swap_index-1], arr[low]
        pivot_index = swap_index-1

        # sort left and right sides from the pivot
        r_qs(arr, low, pivot_index-1)
        r_qs(arr, pivot_index+1, high)

    return arr


# stablilized randomized quicksort
def stable_r_qs(arr):
    if len(arr) <= 1:
        return arr[:]

    # pick random pivot
    pivot_index = randrange(len(arr))
    pivot_val = arr[pivot_index][:2]

    left, equal, right = [], [], []

    # partition
    for name in arr:
        prefix = name[:2]
        if prefix < pivot_val:
            left.append(name)
        elif prefix > pivot_val:
            right.append(name)
        else:
            equal.append(name)  # order preserved

    # recurse
    return stable_r_qs(left) + equal + stable_r_qs(right)


# lst = ['Mozart', 'Beethoven', 'Bach']
# print(r_qs(lst[:]))
lists_of_names = []

while True:
    n = int(input())
    if n == 0:
        break

    lst = []
    for _ in range(n):
        name = input()
        lst.append(name)
    lists_of_names.append(lst)

    # sorted_lst = r_qs(lst[:])
    # for name in sorted_lst:
    #     print(name)

for lst in lists_of_names:
    for name in stable_r_qs(lst[:]):
        print(name)
    print()
