def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()  # Pop method removes last element and also returns it. So, the last number in the sequence becomes the pivot point.

    items_greater = []
    items_lower = []

    for item in sequence:  # For every item left in the sequence
        if item > pivot:
            items_greater.append(item)  # Adds item to items_greater list
        else:
            items_lower.append(item)    # Adds item to items_lower list

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)  # Applies algorithm again to each items_lower and items_greater,
                                                                          # then adds pivot point in between.

print(quick_sort([2, 6, 9, 5, 4, 3, 8, 8, 3, 11, 30, 69]))
