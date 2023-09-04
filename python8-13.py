'''
#exercise8
MyFloatValue= 9.82
MyFloatValue= int(MyFloatValue)
print(type(MyFloatValue))
MyFloatValue= str(MyFloatValue)
print(type(MyFloatValue))

#exercise8(2)
#a='h'
#int(a)
#value error

#exercise9(1,2)
year = int(input("Enter the current year"))
age = int(input("What age will you be at the end of this year?")) # Note the int() cast on the input 
print("You were born in", year-age)

#exercise9(3)
#the first one because python cannot add a srting to a variable

#exercise10
mars=1
m=int (input ('enter no of mars bars'))
coke=1.5
c=int (input ('enter no of coke cans'))
crisps=.8
cr=int (input ('enter no of crisps'))
t=int (input ('enter no of tea'))
tea=2
p=int (input ('enter no of pans'))
pan=3.5
total=mars*m+coke*c+crisps*cr+tea*t+pan*p
print(total)

#exercise11
number1=int(input('enter 1st num'))
number2=int(input('enter 2nd num'))
sum=number1+number2
print (number1,'+',number2,'=',sum)

#exercise12
f=int(input('enter temp in f'))
c=(f-32)*5/9
print('temp in c is',c)
'''

#exercise13
dd=int(input('enter date'))
mm=int(input('enter month'))
year=int(input('enter year'))
y=year%100
c=int(str(year)[0:2])
if (mm==1):
    mm=13
elif (mm==2):
    mm=14
wd=(dd+(13*(mm+1)/5)+y+(y/4)+(c/4)-2*c)%7
print (wd)








