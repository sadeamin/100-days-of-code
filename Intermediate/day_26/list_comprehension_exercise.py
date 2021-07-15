# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
# #
#
# new_numbers = [n ** 2 for n in numbers]
# print(new_numbers)




# result = [n for n in numbers if n % 2 == 0]
# print(result)



with open("file1.txt") as file:
    file_1 = file.readlines()

with open("file1.txt") as file:
    file_2 = file.readlines()

result = [int(num) for num in file_1 if num in file_2]

print(result)

