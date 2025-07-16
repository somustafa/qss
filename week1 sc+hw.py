#Study Case 
#Create a function called "addition_2number" that takes two input numbers from user and returns sum and count of them.
def addition_2number(a,b):
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    return a + b



#Create a function called "addition" that can add two or more numbers till user enters zero and returns answer and count of input numbers in a list.
def addition():
   sum = 0
   count = 0 
   while True:
       a = int(input("enter number: ")) 
       if a == 0:
           break
       sum += a
       count += 1
   return [sum, count]

#Create a function called "subtraction" that can subtract two or more numbers till user enters zero and returns answer and count of input numbers in a list.
def subtraction():
    count_of_numbers = 0
    result = 0
    while True:
        num = int(input("Enter number: "))
        if num  == 0:
            break
        if num is None:
            result = num
        else:
           result = result - num
           count_of_numbers += 1
    return [result, count_of_numbers]



#Create a function called "multiplication" that can multiply two or more numbers till user enters zero and returns answer and count of input numbers in a list.
def multiplication():
    count_of_numbers = 0
    result = 1
    while True:
        num = int(input("Enter number: "))
        if num == 0:
            break
        if num is None:
            result = num 
        else:
            result = result * num
            count_of_numbers += 1
    return [result, count_of_numbers]


#Create a function called “average” that returns mean of “addition” function.
def addition():
   sum = 0
   count = 0 
   while True:
       a = int(input("enter number: ")) 
       if a == 0:
           break
       sum += a
       count += 1
   return [sum, count]
def avarage():
    result = addition()
    total = result[0]
    count = result[1]
    if count == 0:
        return 0
    mean = total /count
    return mean
  

#Create a simple calculator that asks user to perform operations
wanted_op = input("enter your operation: +, -, *, / : ")
if wanted_op == "+":    
    result = addition()
    print(result[0], result[1])
elif wanted_op == "-":
    result = subtraction()
    print(result[0], result[1])
elif wanted_op == "*":
    result = multiplication()  
    print(result[0], result[1])
elif wanted_op == "/":
    result = avarage()
    print(result)
else:
    print("Invalid operation. Please enter +, -, *, or /.")

#Write a Python program to find intersection of two given arrays using lambda.
array1 = [1, 2, 3, 4, 5]
array2 = [4, 5, 6, 7, 8]

intersection = list(filter(lambda x: x in array2, array1))
#filter sayesinde array1 deki elementlere baxiriq ( hemise ikinci argumente baxir) lambda ise array2  deki her br elemente baxir
print("Intersection of the two arrays:", intersection)


#Write a Python program to add two given lists using map and lambda.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list(map(lambda x, y: x + y, list1, list2))
print("Sum of the two lists:", result)

#Write a Python program that stores numbers in a list which are divisible by nineteen or thirteen from a given list.
list = [1, 2, 3, 19, 26, 39, 52, 65, 78, 91]
#1
for i in list:
    if i % 19 == 0 or i % 13 == 0:
        print(i, end=" ")
#2
result = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, list))
print("\nNumbers divisible by nineteen or thirteen:", result)










#Homework;
#1. Create variable age equal to 32 and check its type.
age = 32
print("Type of age:", type(age))

#2.Create variable height equal to 1.85 and check its type.
height = 1.85     
print("Type of height:", type(height))

#3.Create variables name and surname. Define them as 'your_name' and 'your_surname'.
name = "your_name"
surname = "your_surname"

#4.Sum up name and surname variables. Define as ID.
ID = name + " " + surname

#5. Use indexing. Find last letter of 'your_name'.
last_letter = name[-1]

#6. Use slicing. Find 2nd and 3rd letters of 'your_surname'.
letters = surname[1:3]

#7. Create list as new_list. Include 3 4 5 6 7 integers.
new_list= [3, 4, 5, 6, 7]

#8. Remove 5 from new_list. 
new_list.remove(5)

#9. Delete 2nd value of new_list.
del new_list[1]

#10.Create tuple as new_tuple. Include 3 4 5 6 7 integers.
new_tuple = (3, 4, 5, 6, 7)

#11. Change 4 to 8 in new_tuple.
new_list = list(new_tuple) # tuple in icinde birbasa deyismek olmur deye liste cevirib deyisirik sonra yene qaytaririq tupple'a
new_list[1] = 8
new_tuple = tuple(new_list)


#Optional Questions:
#1. Find the difference between age and 25, if the number is greater than 17 return the square of the difference.
age = int(input("enter your age: "))
c = abs(age-25)
if c > 17:
    print(c**2)

#2. Write a Python function to check number is positive, negative or zero.
num  = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")    