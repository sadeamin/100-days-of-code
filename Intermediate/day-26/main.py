# list Comprehension
#
# numbers = [1, 2, 3, 4, 5]
# new_list = [n + 1 for n in numbers]
# print(new_list)
#
# name = "Eamin"
# letter_list = [letter for letter in name]
# print(letter_list)
#
# double_num_list = [num * 2for num in range(1, 5+1)]
# print(double_num_list)

names = ["Alex", 'Beth', "Caroline", "Dave", "Elanor", "Freddie"]
short_name = [name for name in names if len(name) < 5]
print(short_name)

upper_names = [name.upper() for name in names if len(name) > 5]
print(upper_names)