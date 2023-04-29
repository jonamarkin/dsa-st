
# First solution
# This solution uses recursion to solve the problem.
def add_digits(num):
    if num < 10:
        return num
    else:
        return add_digits(sum([int(i) for i in str(num)]))


print("Adding digits of 38: ", add_digits(38))


# Second solution
# Use the digital root mathematical formula to solve the problem.


def add_digits_2(num):
    if num == 0:
        return 0
    else:
        return (num - 1) % 9 + 1


print("Adding digits of 38: ", add_digits_2(38))
