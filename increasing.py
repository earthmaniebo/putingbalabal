arr_num = [
    [1, 2, 3, 4, 5],  # out: True
    [10, 1, 2, 3, 4, 5],  # out: True
    [10, 1, 2, 3, 8, 5],  # out: False
    [1, 2, 3, 8, 5],  # out: True
    [1, 2, 3, 8, 5, 7],  # out: True
    [1, 2, 3, 8, 5, 7, 6, 7],  # out: False
    [1, 2, 3, 8, 2, 7],  # out: False
    [1, 2, 5, 8, 4, 7],  # out: False
    [1, 2, 5, 8, 4, 9, 20],  # out: True
    [1, 2, 3, 9, 4, 11],  # out: True
    [1, 2, 3, 2, 4, 5, 6],  # out: True
    [1, 4, 5, 2, 41, 51, 61],  # out: True
    [1, 2, 3, -3, 5, 7],  # out: True
    [1, 2, 3, 4, 99, 6, 7, 8, 9, 10, 11],  # out: True
]


def run():
    # loop into the array of arrays of integers
    for num_list in arr_num:
        '''
        Keep track of the number of times we need to remove an element. If the
        value is greater than 1, then automatically is_increasing is False.
        '''
        false_count = 0
        is_increasing = True
        num_list_len = len(num_list)

        # take note of the highest number in the array
        highest_num = max(num_list)

        # loop for numbers in an array
        for i in range(0, num_list_len):
            current = num_list[i]

            # current index is not the last element
            if i + 1 != num_list_len:
                upnext = num_list[i + 1]
                if current > upnext:
                    if i != 0:
                        previous = num_list[i - 1]
                        if previous > upnext and current >= highest_num:
                            '''
                            Additional checking if the next element is lower
                            than the previous element but the current element
                            is the highest number in the array.
                            '''
                            false_count = false_count + 1
                    false_count = false_count + 1

            # last element
            else:
                previous = num_list[i - 1]
                if current < previous and false_count == 0:
                    '''
                    Check if we can remove the last number for it to be
                    increasing. Also, we can check if the second to the last
                    number is the element needed to be removed.
                    Why test if false_count == 0? See the examples below:

                    a = [10, 20, 30, 40, 5] // should be true
                    b = [1, 2, 3, 8, 5] // should be true

                    For array a, 5 < 40 and current value of false_count is 0.
                    Given that, it's ok to assume that it's the only element
                    preventing the array from being classified as increasing.

                    However for array b, it gets tricky.

                    From the other if condition above: (if current > upnext)
                    evaluates to 8 > 5 thus setting false_count = 1.
                    Then, (if current < previous) evaluates to 5 < 8 but
                    instead of incrementing false_count again, check if the
                    previous number is also the one who's been flagged earlier.
                    '''
                    false_count = false_count + 1

            # break out of loop if there are more than 1 element to be removed
            if false_count > 1:
                is_increasing = False
                break

        # Pretty print the output for betting checking
        print num_list, '->', is_increasing


def main():
    run()


if __name__ == '__main__':
    main()
