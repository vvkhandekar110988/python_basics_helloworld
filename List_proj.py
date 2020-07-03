''' Find the lasrgest number in the list'''
def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max

numbers = [12, 45, 6, 89, 16, 75]
print(max)

