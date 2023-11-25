# Question 16(a)
# Name and School:
import random

while True:
    s_name=input("Enter your surname:      ")    
    f_name=input("Enter your first name:      ")
    age=int(input("Enter your age:      "))
 
 
    eir=input('enter your eir code')
    s=input("do you agree to enroll in a vaccine trial 'yes' or 'no'")
    if age>11 and age<50:
        vaccine='MRNA'
    elif age>=50:
        vaccine='ADENO'
 
    if int(eir[len(eir)-1])%2==0:
        centre='eastwood'
    else:
        centre='northfield'
 
    print("Hello", f_name, s_name,'you are ',age,'years old and your eir code is ',eir)		#1
    if s=='yes':
        choice=('A','B','C')
        print('You are now enrolled in the trial to recieve super vaccine',random.choice(choice))
    print('You must attend ',centre,'for your vaccine')
    print(f_name,'you will recieve the ',vaccine,' vaccine')
    details=input("If you have finished entering people's details type 'END', otherwise press RETURN:")
    if details=='END':
        break