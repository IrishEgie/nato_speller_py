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
with open("file1.txt") as file1:
    content = file1.readlines()

with open("file2.txt") as file2:
    lines = file2.readlines()
int_list = [int(num) for num in content]
stuff = [int(same) for same in lines]
result = [match for match in int_list if match in stuff]
print(result)