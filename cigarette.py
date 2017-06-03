def cigarette(n, k):
    consumed = 0
    cigar_butts = 0

    # loop until you ran out of cigar
    while n != 0:
        # light a cigar
        consumed = consumed + 1

        # cigar extinguished
        cigar_butts = cigar_butts + 1

        # reset cigar butts count and add a new cigar in your inventory
        if cigar_butts == k:
            n = n + 1
            cigar_butts = 0
        n = n - 1
    return consumed


def main():
    print cigarette(n=8, k=3)
    print cigarette(n=3, k=3)
    print cigarette(n=24, k=5)
    print cigarette(n=102, k=5)
    print cigarette(n=259, k=7)
    print cigarette(n=10, k=2)


if __name__ == '__main__':
    main()
