#WAP to find the prime no
'''
num = 10
for i in range(2,num):
  if num %i == 0:
   print("Not prime")
   break
else:
    print("prime")
_________________________________________________________________
# Print First 10 natural numbers using while loop

i=1
while i<=10:
    print(i)
    i+=1
______________________________________________
#Print the following pattern
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

for row in range(1,6):
    for col in range(1,row+1):
        print(col,end = '')
        print("")
________________________________________
#Calculate the sum of all numbers from 1 to a given number

n=input("Enter Number")
n=int(n)
sum=1
for num in range(1,n+1):
    sum=sum+num
    print("Sum Of first","number is:",sum)
_____________________________________________________________
#Write a program to print multiplication table of a given number

n=int(input("Enter the no to print mul of table:"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)12
_______________________________________________
#Write a program to display only those numbers from a list that satisfy the following conditions

#The number must be divisible by five
#If the number is greater than 150, then skip it and move to the next number
#If the number is greater than 500, then stop the loop
#numbers = [12, 75, 150, 180, 145, 525, 50]

for i in num:
    if i>500:
        break
    else:
        if i%5==0:
            if i>150:
                continue
            else:
                print(i)
__________________________________________________________

for i in numbers:
    if i>500:
        break
    elif i>150:
        continue
    elif i%5==0:
        print(i)
_____________________________________________________

#Count the total number of digits in a number
n=int(input("Enter number:"))
count=0
while(n>0):
    count=count+1
    n=n//10
    print("The no of digits in the no are:",count)
__________________________________________________
#Print the following pattern
#5 4 3 2 1
#4 3 2 1
#3 2 1
#2 1

for i in range (5,0,-1):
    for j in range (i,0,-1):
        print (j, end=' ')
    print()
______________________________________________
#Print list in reverse order using a loop

#list1 = [10, 20, 30, 40, 50]
def Reverse(lst):
    lst.reverse()
    return lst


lst = [10, 20,30,40,50]
print(Reverse(lst))
_________________________________________________
#Display numbers from -10 to -1 using for loop
#Use else block to display a message “Done” after successful execution of for loop

a=0
b=0
print(a,end='')
print(b,end='')
for i in range(1,9):
    s=a+b
    print(s, end='')
    a=b
    b=s
________________________________________________________
#Find the factorial of a given number
num=int(input('enter a number'))
f=1
for i in range(1,num+1):
  f=f*i
print ('factorial of', num, '=',f)
____________________________________________

#Reverse a given integer number
a = input("Enter Number ")

s=''
for i in range(len(a)-1,-1,-1):
    s= s+a[i]
print(s)
________________________________________________
# Use a loop to display elements from a given list present at odd index positions

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# stat from index 1 with step 2( means 1, 3, 5, an so on)
for i in my_list[1::2]:
    print(i, end=" ")
________________________________________________
#Calculate the cube of all numbers from 1 to a given number

input_number = 6
for i in range(1, input_number + 1):
    print("Current Number is :", i, " and the cube is", (i * i * i))
_________________________________________________
#Find the sum of the series upto n terms
Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
n = 5
start = 2
sum_seq = 0
for i in range(0, n):
    print(start, end="+")
    sum_seq += start
    start = start * 10 + 2
print("\nSum of above series is:", sum_seq)
________________________________________
  #OR
a=2
s=0
n=5
for i in range (1,n+1):
    s= s+ int(str(a)*i)
print(s)
______________________________________
#Print the following pattern
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")
_________________________________________________
#OR
for i in range (1,6):
    print (i*'* ')
for i in range (4,0,-1):
    print (i*'* ')
________________________________________________________

# print a pattern
1
1 2
1 2 3
1 2 3 4


n = int(input("Enter the no of rows:"))
for i in range(n):
    for j in range(i+1):
        print(j+1,end = ' ')
    print()
______________________________________
#OR

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end= " ")
    print()
________________________________
size = 4
for i in range(size):
      for j in range(1, size-i):
        print(" " ,end = " ")
    for j in range(i+1):
         print(j + 1, end = " ")
    print()
____________________________________________
################### FUNCTION #############

# Write a function  input a no then its print multiplication table.

def print_table(num):
    for i in range(1,11):
        print(num,' x ', i, ' = ',num*i)
n = int(input(" print its multiplication table:"))
print_table(n)
________________________________________________

#Write a program to print twin prime number less than 1000.

def isPrime(a) :
    count = 0
    for i in range(2, a+1) :
        if a % i == 0 :
            count = count + 1
    if count == 1:
            return True
n = 2
N = int(input("Enter the value of N : "))
while n < N :
    if isPrime(n) == True and isPrime(n+2) == True:
        print("({0},{1})".format(n, n+2), end = "    ")
    n = n + 1
_________________________________________________

OR
def prime (a):

    if a < 3:
        return False
    else:
        for i in range (2,a):
            if a%i == 0:
                return False
        else:
            return True
for i in range(1000):
    if prime(i) == True and prime (i+2) == True:
        print(i,i+2)
__________________________________________________________
#Write program for prime factor of number

def prime_fac(a):
    for i in range(2, a):
        while a % i == 0:
            print(i, end=" ")
            a = a // i
    else:
        if a>1:
    print(a)
_______________________________

def prime_fac(a):
    for i in range(2, a):
        while a % i == 0:
            print(i, end = " ")
            a = a // i
    else:
        if a>1:
         print(a)
prime_fac(56)
________________________________________
# Write a program to perform permutation and combination
#write a function that converts a number from decimal to binary



def Dec_to_bin(num):
    decimal_num = bin(num).replace("0b", "")
    print(decimal_num)


Dec_to_bin(13)
__________________________________________
##### OR ############

def bin(a):
    s=''
    while a>0:
        s += str(a % 2)
        a=a//2
    return s[::-1]
print(bin 10)
___________________________________
#An Armstrong number, also known as narcissistic number, is a number that is equal to the sum of the cubes of its own digits. For example, 370 is an Armstrong number since 370 = 3*3*3 + 7*7*7 + 0*0*0

def cubesum(a):
    sum= 0
    for i in str(a):
        sum+= int(i)**3
    return sum

def isArmstrong(a):
    if cubesum(a)==a:
        return True
    else:
        return False
_________________________________
# Write a function prodDigits() that returns product of digits of given number

num = int(input("Enter any number : "))

temp = num
product = 1;

while(temp != 0):

    product = product * (temp % 10);

    # Remove last digit from temp.
    temp = int(temp / 10)

print("\nProduct of all digits in", num, ":", product)
__________________________________________________
#OR#########

def prodDigits(n):
    mul=1
    for i in str(n):
        mul*= int(i)
    return  mul
print(prodDigits(21))
____________________________________________
# Using prodDigits() write a program for MDR () and Mpersistence()
#Write a function sumPdivisors() that finds the sum of proper divisors of a number.
## Proper  divisors of a number are those numbers by which the number is divisible, except the  number itself.
'''


















