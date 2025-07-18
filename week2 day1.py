#Case Study
#1. Create a regex that can select names and ages from the given list and create a new dictionary with name as a key and age as a value:
import re

text = """ 
Janice is 22 and Theon is 33
Gabriel is 44 and Joey is 21
Qabil is 555
"""
matches = dict(re.findall(r'([A-Za-z]+)\s+is\s+([0-9]{1,3})', text))
print(matches)


#Create a regex for email verification. meow@gmail.com is a right mail but, Hello.com, MrMu@.com are not.
correct = "meaow@gmail.com"
wrong = "Hello.com", "MrMu@.com"
print(re.findall(r'[A-Za-z0-9]{3,10}@[A-Za-z]{2,10}\.[A-Za-z]{2,4}', correct))


#Create a regex for number verification. (257) 563-7401, (111) 222-3333 are right numbers but, (1) 19-39, +994 012-13-32 are not right numbers.
correct_numbers = "(257) 563-7401 (111) 222-3333"
wrong_numbers = "(1) 19-39, +994 012-13-32"
print(re.findall(r'\([0-9]{3}\)\s[0-9]+-[0-9]+',correct_numbers))



#Homework
#1)Create a Python program which matches a word containing vowels in it (a,ı,o,u,e,ə,i,ö,ü).

vowels = "aıoueiəöü"
text = "Salam, bu qwdds qizin fdkf adi gdksl Sonadir bbb"

pattern = rf'\b\w*[{vowels}]\w*\b'

result = re.findall(pattern, text)
print(result)

#Which matches a word containing vowels not at the start or end of the word (a,ı,o,u,e,ə,i,ö,ü).
vowels = "aıoueiəöü"
text = "Salam qrm nslk bcd qizin adi gdksl Sonadir bbb ekmek uk"

pattern = rf'\b[^{vowels}\W]\w*[{vowels}]\w*[^{vowels}\W]\b'

matches = re.findall(pattern, text)
print(matches)

#Checks for a number at the end of a given string
import re

text1 = "Bu gun ders 2025"
text2 = "Bu gun ders olacaq"

result = re.findall(r'\d+$',text2)
if result == []:
    print("No number found at the end of the string.")
else:
    print("No number found at the end of the string.")  



#4. Which matches a word at the end of string, with optional question mark and exclamation point.
text = "Hello world! How are you? I am fine."
result = re.findall(r'\w+[.!?]', text)
print(result)


#5.Replaces whitespaces with a tab and vice versa.
text = "Hello World! How are you?"
result = re.findall(r'\s', text)
if result:
    text = text.replace(' ', '---')
print(text)

#6.Finds all words starting with 'ə' or 'ü' in a given string.
text = "Əli və Ümid məktəbə gedir. Ən sevdiyim rəng üstdür."
result = re.findall(r'\b[ƏəüÜ]\w+', text)
print(result)


#7Removes all whitespaces from a string.
text = "Hello   world! How are you?"
result = re.sub(r'\s+', '', text)
print(result)

#8.Finds all words which have more than 4 characters in a string.
text = "Hello world! How are you doing today?"
result = re.findall(r'\b\w{5,}',text)
print(result)

#Inserts spaces between words starting with capital letters.
text = "HelloWorldHowAreYou"
result = re.sub(r'(?<!^)(?=[A-Z])', ' ', text)
print(result)