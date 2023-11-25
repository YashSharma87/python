list1=[4,5,9,8,10,17,99,77]
list1.sort()
length=len(list1)

if length%2==0:
    median=(list1[int(length/2)]+list1[int(length/2-1)])/2
else:
   median=list1[int((length-1)/2)]
print(median)