#1. Print First 10 natural numbers using while loop.
a = 1
while a <= 10:
    print(a, end=' ')
    a += 1 
#2. Display -10 to -1 using for loop.
a = -10
for i in range(a, 0):
    print(i, end=' ')
#3. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
for i in range(7):
    if i == 3 or i == 6:
        continue
    else:
        print(i, end=' ')
#4. Calculate the sum of all number between 1 and 111.
sum = 0
for i in range(1, 112):
    sum += i
print(sum)

#5. Reverse the following list using for loop:
list1 = [10, 20, 30, 40, 50]
for i in range(len(list1)-1, -1, -1):
    print(list1[i], end=' ')

#6. Write a Python program to find those numbers which are divisible by 7 and 5, between 1500 and 2700 (both included).
numbers = []
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        numbers.append(i)
print(numbers)

#8. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result
x = 14
y = 3
add_fifteen = lambda x: x + 15
multiply = lambda x, y: x * y

#9. Write a Python program to square and cube every number in a given list of integers using Lambda.
list = [1,2,3,4,5]
square = list(map(lambda x: x**2, list))
cube = list(map(lambda x: x**3, list))

#10. Write a lambda function that returns takes x as parameter and returns x+2. Then assign into a variable named L.
l = list(map(lambda x: x+2, list))

#11. Write a function which takes two arguments: a and b and returns the multiplication ofthem: a*b. Assign it to a variable named f.
def multi(a,b):
    return a * b
a = int(input())
b = int(input())
print(multi(a, b))

#12. Write a Python program to add two given lists using map and lambda.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list(map(lambda x, y: x + y, list1, list2))
print("Sum of the two lists:", result)

#13. Write a map function that adds plus 5 to each item in the list.
list3 = [1, 2, 3, 4, 5]
result = list(map(lambda x: x + 5, list3))

#14. Write a map function that adds "Hello, " in front of each item in the list.
list4 = ["sona", "guler", "veli", "sahib", "fidan"]
result = list(map(lambda x: "Hello, " + x, list4))

#15. Using map() function and len() function create a list that's consisted of lengths of each element in the first list.
list4 = ["sona", "guler", "veli", "sahib", "fidan"]
lenghts = list(map(lambda x: len(x), list4))

#16. Using map() function and lambda add each elements of two lists together. Use a lambda with two arguments.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list(map(lambda x, y: x + y, list1, list2))

#17. Using map() , lambda and count() functions create a list consisted of the number of occurrence of letter: a.
words = ["apple", "banana", "grape", "avocado", "berry"]
result = list(map(lambda x: x.count('a'), words))

#18. Using map(), lambda and count() functions create a list consisted of the number of occurrence of both letters: A and a.
words = ["Apple", "banana", "grApe", "avocado", "berry"]
result = list(map(lambda x: x.count('a') + x.count('A') , words))

#19.  Using filter() function filter the list so that only negative numbers are left.
list5 = [1, -2, 3, -4, 5, -6]
result = list(filter(lambda x: x < 0, list5))

#20. Using filter function, filter the even numbers so that only odd numbers are passed to the new list.
list6 = [1, 2, 3, 4, 5, 6]
new_list = list(filter(lambda x: x%2 != 0, list6))
 
#21. Using filter() and list() functions and .lower() method filter all the vowels in a givenstring.
string = "Hello World"
vowels = 'aeiou'
result = list(filter(lambda x: x.lower() in vowels, string))

#22.This time using filter() and list() functions filter all the positive integers in the string.
string2 = "Hello 123 World -456"
integers = '0123456789'
#1
result = list(filter(lambda x: x.isdigit() and int(x) > 0, string2.split()))
#2
result = list(filter(lambda x: x.isdigit() and int(x) > 0, string2.split()))

#23. Using map() and filter() functions add 2000 to the values below 8000.
values = [5000, 7000, 8000, 9000, 10000]
result = list(map(lambda x: x + 2000 if x < 8000 else x, values))

#24.Write a Python program to count the even, odd numbers in a given array of integers using Lambda.
integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count_even = list(filter(lambda x: x % 2 == 0, integers))
count_odd = list(filter(lambda x: x % 2 != 0, integers))

#25.Write a Python program to filter a given list whether the values in the list are having length of 6 using Lambda.
list7 = ["apple", "banana", "cherry", "kiwi", "mango"]
result = list(filter(lambda x: len(x) == 6, list7))

#26. Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.
my_list = [1, 2, 3, 19, 26, 39, 52, 65, 78, 91]
result = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, list))

#27. Using zip() function and list() function, create a merged list of tuples from the two lists given.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list(zip(list1, list2))

#28. 28. First create a range from 1 to 8. Then using zip, merge the given list and the range together to create a new list of tuples.
r = range(1,9)
my_list = [10, 20, 30, 40, 50, 60, 70, 80]
merge = list(zip(r,list))

#29. Using zip and dict functions create a dictionary which has its key-value pairs comingfrom lst1 and lst2.
lst1 = ['name', 'age', 'city']
lst2 = ['Aysel', 25, 'Baku']
result_dict = dict(zip(lst1, lst2))

#30 Using zip, list and sorted functions create a sorted list of tuples from lst1 and lst2.
lst1 = [3, 1, 4]
lst2 = ['c', 'a', 'b']

zipped = zip(lst1, lst2)
zipped_list = list(zipped)          
sorted_list = sorted(zipped_list)   

print(sorted_list)
