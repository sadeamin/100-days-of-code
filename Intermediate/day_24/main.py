# with open("my_file.text") as file:
#     contents = file.read()
#     print(contents)

# with open("my_file.text", mode="w") as file:
#     file.write("\nNew text.")


with open("my_file.txt", mode="a") as file:
    file.write("\nnew text")

# with open("new_file.text", mode="w") as file:
#     file.write("\nHi.")