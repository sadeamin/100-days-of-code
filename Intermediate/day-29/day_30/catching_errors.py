try:
    file = open("C:/Users/Eamin/PycharmProjects/100-days-of-code/Intermediate/day-29/day_30/a_file.txt")
    a_dictionaty = {"key": "value"}
    print(a_dictionaty["key"])
except FileNotFoundError:
    file = open("C:/Users/Eamin/PycharmProjects/100-days-of-code/Intermediate/day-29/day_30/a_file.txt", "w")
    file.write("Something")

except KeyError as error_message:
    print(f"That {error_message} does not exist.")
else:
     content = file.read()
     print(content)

finally:
    file.close()
    print("File was closed.")