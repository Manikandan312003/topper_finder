#Topper Problem
def topper_finder(topper_number):
    odd, even = 0, 0
    while topper_number:
        if topper_number % 2 == 0:
            even += topper_number % 10
        else:
            odd += topper_number % 10
        topper_number //= 10
    return 'true' if odd==even else 'false'
n=int(input())
print(topper_finder(n))