# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# #
# splited_sentence = sentence.split(" ")
# result = {word: len(word) for word in splited_sentence}
# print(result)



# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24
# }
#
# weather_f = {day: (temp_c * 9 / 5 + 32) for (day, temp_c) in weather_c.items()}
# print(weather_f)

# How to iterate over a Pandas DataFrame

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]

}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key, value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Looping through pandas DataFrame:
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.student, row.score)