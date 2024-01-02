# Print out a pattern like this programmatically with n
# n = the number of star equivalent to how wide the wing is
# there is 1 space in between the * on each line
# eg. in this case n = 4
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
#
# eg. in this case n = 1
# *
# * *
# *
def print_pattern(n: int):
    # ========================================================================
    # My code uses 1, 4 and 10 rows of * to get the output. If I have time I need to try again using nesting
    for i in range(1, n + 2):  # first half
        print("* " * i)
    for i in range(n , 0, -1):  # second half
        print("* " * i)


def main():
    print_pattern(1)
    print_pattern(4)
    print_pattern(10)


if __name__ == "__main__":
    main()