def max_activity_selected(start, finish):
    count_activity = len(start)
    i = 0
    count_selected = 1
    for j in range(count_activity):
        if start[j] >= finish[i]:
            count_selected += 1
            i = j
    return count_selected


# activity has been sorted first by finish time
print(max_activity_selected(start=[1, 3, 0, 5, 3, 5, 6, 7, 7, 2, 12],
                            finish=[4, 5, 6, 7, 9, 9, 10, 11, 12, 13, 16]
                            ))
