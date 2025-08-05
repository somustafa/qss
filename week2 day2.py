#Case Study 
#1)Create an array of 20 linearly spaced points between 0 and 1.
import numpy as np

arr = np.linspace(0, 1, 20)
#print(arr)

#2) Create a 5x5 matrix from 1 to 25 and sum the columns' numbers.
a = np.arange(1, 26).reshape(5, 5)
#print(a)
b= a.sum(axis=0)
#print(b)

#3)Create the following matrix. - 0dan 1e qeder 0.1 artaraq gedir. \
z = np.arange(0.01, 1.01, 0.01).reshape(10, 10)
#print(z)

#4)4) Follow the steps:
#A) Define a structured data type ( name - S20, Surname - S20, age-i1, mark-f4)
#B) Create an array with the given information below in a data type created
#(Behram Abbasov 26 85, Yusif Abdullayev 22 92, Maryam Mecidova 19 88, Vagif Hesenzade 24 79)
dt = np.dtype([('name', 'S20'), ('surname', 'S20'), ('age', 'i1'), ('mark', 'f4')])
data = np.array([
    ('Behram', 'Abbasov', 26, 85),
    ('Yusif', 'Abdullayev', 22, 92),
    ('Maryam', 'Mecidova', 19, 88),
    ('Vagif', 'Hesenzade', 24, 79)
], dtype=dt)

#print(data)


#5) Create a matrix
x = np.zeros((10,10), dtype=int)
x [0, :] = 99
x[-1, :] = 99
x[: , 0] = 99
x[:, -1] = 99
x [1,1] = 98
x[1, -2] = 98
x[2, 2:8] = 1
x[3, 2] = 1
x[3, 7] = 1
x[4, 2] = x[4, 7] = 1
x[4, 4] = x[4, 5] = 1
x[5, 2] = x[5, 7] = 1
x[5, 4] = x[5, 5] = 1
x[6, 2] = x[6, 7] = 1
x[7, 2:8] = 1
x[8, 8] = 1

#print(x)




#Homework
#1)Create a vector with values ranging from 15 to 55 and print all values except the first and last.
v = np.arange(15, 55)
v = v[1:-1]
#print(v)

#2)Create a 3X4 array using np.full().
arr = np.full((3, 4), 7)

#3)Create a 3x3 matrix filled with values from 10 to 18. Use np.arange() and np.reshape().
arr = np.arange(10, 19).reshape(3, 3)
#print(arr)

#4)Create a 5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4, 5 using np.diag().
d = np.zeros((5,5))
elements = np.array([1, 2, 3, 4, 5])
d = np.diag(elements)
#print(d)

#5)Create a null vector of size 10 using np.zeros() and update sixth value to 11.

v = np.zeros(10)     # 10 elementli sıfırlardan ibarət vektor
v[5] = 11           # 6-cı elementə 11 qiymətini ver (indeks 5-dir)

#print(v)

#6)Convert an array to a float type using np.asfarray().
arr = np.array([1, 2, 3, 4, 5])
float_arr = np.asarray(arr)
#print(float_arr)   

#7) Swap columns in a given array.
arr = np.array([[0, 1, 2, 3],
                [4, 5, 6, 7],
                [8, 9, 10, 11]])
arr = arr[:, :: -1]
#print(arr)  


#8) Capitalize the first letter, lowercase, uppercase, swapcase, title-case of all the elements of a given array. Use np.char.capitalize(), np.char.lower(), np.char.upper(), np.char.swapcase(), np.char.title().
arr = np.array(['hello', 'world', 'python'])
capitalized = np.char.capitalize(arr)
lowered = np.char.lower(arr)
uppered = np.char.upper(arr)
swapped = np.char.swapcase(arr)
titled = np.char.title(arr)


#9)Get the dates of yesterday, today and tomorrow using np.datetime64() and np.timedelta64().
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
today = np.datetime64('today', 'D')
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')

#10)10.Append values to the end of an array using np.append().
#Original array: [10, 20, 30]
#Expected Output: [10 20 30 40 50 60 70 80 90]
arr = np.array([10, 20, 30])
new_values = np.array([40, 50, 60, 70, 80, 90])
appended_arr = np.append(arr, new_values)
#print(appended_arr)






# --------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
cars = pd.read_excel('cars.xlsx')   

#1. Show relationship between horsepower and city miles per gallon.
#a. Use scatter in matplotlib.
#b. Interpret how are variables correlated according to scatter.

plt.scatter(cars['cty'], cars['hwy'])
plt.xlabel('city')
plt.ylabel('horsepower')
plt.title('horsepower and city miles per gallon.')
#plt.show()


#2.Show distributions and scatters between all variables. While hue equals to type of drive train which variables have the lowest and the highest correlation? Find according to scatterplot.
sns.pairplot(cars, hue='drv')
#plt.show()

#3. Which type of car is most frequent in dataset? Show by using countplot.
plt.figure(figsize=(10,6))
sns.countplot(x='class', data=cars)
plt.xticks(rotation=45)
plt.show()

#4.Display number of cylinders for each drive train in bar chart. Which drive train is the most frequent?
plt.figure(figsize=(10,6))
sns.countplot(data=cars, x='cyl', hue='drv')
plt.show()
print(cars['drv'].value_counts())

#5)Visualize engine displacement by each class using boxplot. Do the same thing in violinplot.
plt.figure(figsize=(14, 6))

# Boxplot - mühərrik həcmi üzrə hər Class üçün
plt.subplot(1, 2, 1)
sns.boxplot(data=cars, x='class', y='displ')
plt.title('Engine Displacement by Car Class (Boxplot)')
plt.xticks(rotation=45)

# Violinplot - eyni məlumatı başqa vizual formada göstərir
plt.subplot(1, 2, 2)
sns.violinplot(data=cars, x='class', y='displ')
plt.title('Engine Displacement by Car Class (Violinplot)')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()