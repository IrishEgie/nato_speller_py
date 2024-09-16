# numbers = [1,2,3]

# new_list = [n+1 for n in numbers] #list comprehension

# for n in numbers:
#     add1 = n+1
# new_list.append(add1)

# #multiplier list in list comprehension
# mul_list  = [n*2 for n in range(1,5)]
# print(mul_list)

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# long_names = [name.upper() for name in names if len(name)>4]
# print(long_names)

## exercise 1
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num**2 for num in numbers]
# print(squared_numbers)

## exercise 2
# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(n) for n in list_of_strings] #convert the string list to int here
# result = [num for num in numbers if num%2==0] #only even numbers here
# print(result)

## exercise 3
# with open("file1.txt") as file1:
#     content = file1.readlines()

# with open("file2.txt") as file2:
#     lines = file2.readlines()
# int_list = [int(num) for num in content]
# stuff = [int(same) for same in lines]
# result = [match for match in int_list if match in stuff]
# print(result)

## exercise 4
# import random as rd
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# students_scores = {student:rd.randint(0,15) for student in names}
# passed_students = {student for (student, score) in students_scores.items()  if score > 10 }

# print(students_scores)
# print(passed_students)

##exercise 5
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# words = sentence.split()

# result = { letters: len(letters) for letters in words}
# print(result)

# #exerise 6 
# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

# weather_f = { day:(c * 9/5) + 32 for(day, c) in weather_c.items()}

# print(weather_f)