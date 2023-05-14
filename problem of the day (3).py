array = [1, 2, 7, 5, 8, 2, 1]

for number in array:
    if array.count(number) == 1:
        print("The number that appears only once in the array is:",number)
        break