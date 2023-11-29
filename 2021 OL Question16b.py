# Question 16_b
# Student Name: 

Standard_Postal_List=['Netherlands', 'Denmark','Poland', 'Portugal', 'Finland', 'Romania', 'France', 'Germany', 'Greece', 'Spain', 'Hungary', 'Sweden', 'Ireland']
country=input('Please enter the country that you wish to send the order to: ')
if country in Standard_Postal_List:
    print('This country uses standard postage and packaging costs')
else:
    print('This country is not on the approved delivery list')
    add=input('Would you like to add this country to the approved Postal List for future deliveries, y/n: ')
    if add=='y':
        Standard_Postal_List.append(country)
        print(country,' has been added to the Standard Postal List')
    elif add=='n':
        print(country,' has NOT been added to the Standard Postal List')
Standard_Postal_List.sort()
print(Standard_Postal_List)