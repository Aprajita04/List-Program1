#Write a program to display the largest word from the string.
'''
l=[]
s='python is very good language'
for i in s.split():
    l.append(len(i))
for j in s.split():
    if len(j)==max(l):
         print(j)
_________________________________________________
2#Write a program to accept a string and display it in upper case.
str=input("Enter any String :")
print(str.upper( ))
______________________________
#3Write a program to display the unique words from the string.
s= input("Enter String: ")
print(list(set(s.split())))
__________________________________________________________
#4Write a program to accept a string and display the ascii value of each character.

s=input("Enter the string:")
print([(i,ord(i))for i in s])
output:Enter the string:Aprajita
[('A', 65), ('p', 112), ('r', 114), ('a', 97), ('j', 106), ('i', 105), ('t', 116), ('a', 97)]
_______________________________________________________________________________
#5 Write a program to accept a string and replace all spaces by ‘#’ symbol.
'
string = "Once in a blue moon";
for i in string:
      if i.isspace():
          string=string+'#'
      else:
          string=string+i
print(string);
#0r

s=input("Enter string:")
a=s.split()
print('#'.join(a))
print(s.replace('','#'))
_____________________________________________________

#6 Write a program to accept two strings from the user and display the common words.(Ignore case)

 # solving by set
s1=input("Enter the string:")
s2=input("Enter the string:")
set1=set(s1.lower().split())
set2=set(s1.lower().split())
print(set1.intersection(set2))
#output:
#Enter the string:python is very good language
#Enter the string:PYTHON IS A VERY GOOD LANGUAGE
#{'language', 'python', 'is', 'very', 'good'}
__________________________________________________________
#7 Write a program to accept a string and count the frequency of each vowel.
sentence=input("enter the string:")
string=sentence.lower()
print(string)
count=0
list={"a","e","i","0","u"}
for char in string:
    if char in list:
        count=count+1
print("no of vowels :",count)
output:-enter the string:python is very good language
python is very good language
no of vowels : 6
_____________________________________________________________
###################OR############################

s1=input("Enter string:")
d={}
for i in {'a','e','i','o','u'}:
     d[i]=s1.lower().count(i)
print(d)

#output#
Enter string:hello world
{'u': 0, 'i': 0, 'a': 0, 'o': 2, 'e': 1}
_________________________________________________
#8Write a program to display the smallest word from the string.
s1 = input("Enter String: ")
l=[]
for i in s1.split():
    l.append(len(i))
for j in s1.split():
    if len(j) == min(l):
        print(j)
_________________________________________________
9# Write a program to accept a string and display the string with changed case.(Change upper case alphabet to lower case and vice versa)

str=input("Enter any String :")
print(str.swapcase())
______________________________________
#10Write a program to accept a string and display the string in Title case. (first alphabet of each word in upper case)
str=input("Enter any String :")
print(str.title())

























