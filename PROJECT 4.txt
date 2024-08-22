""" PYHTON MINI PROJECT OR ASSIGNMENT GIVEN BY MAYANK SAXENA SIR JI """

""" TOPIC -> Write a python a program that implements the inventory management system using dictionaries. The program should
             provide the following functionalities :
"""
# => A) ADD A PRODUCT : Allow user to add a product with a unique ID,name,price and quantity'
print("________________________________________________________________________")
print("                             ADD A PRODUCT                              ")
print("________________________________________________________________________")

n = eval(input("enter total product you want to add : "))
dt = {}

# code to get data of students from user 
for i in range(1,n+1):
    print(f"Enter details of product-{i} : ")
    a = input("enter name -> ")
    b = int(input("enter price -> "))
    c = input("enter quantity -> ")
    dt.update({f"st{i}":{"name":a,"price":b,"quantity":c }})

# code to print the data of students provided by the user
print("\nTHE DETAILS OF PRODUCTS ARE :- ")
print("=>ID.- Name - Price - Quantity  <=")
for i in range(1,n+1):
    print(" ",i,")",sep="",end=" ")
    print("  ",dt[f"st{i}"]["name"],dt[f"st{i}"]["price"],dt[f"st{i}"]["quantity"],sep=" => ")
print()    

# => B) REMOVE A PRODUCT : Allow user to remove an existing product by specifying the product ID 
print("________________________________________________________________________")   
print("                           REMOVE A PRODUCT                             ")
print("________________________________________________________________________")

term = int(input("Enter total product whose details you want to delete : "))
lst = []     # in this we will store the roll number which we will delete
for i in range(1,term+1):
    roll = int(input("Enter the id : "))
    dt.pop(f"st{roll}")
    lst.append(roll)

print("\nTHE DETAILS OF PRODUCTS AFTER MODIFICATION ARE :- ")

for i in range(1,n+1):
    check = 0
    for j in range(term):
        if i == lst[j] :  
             check = 1       
    if check == 0 :
        print(" ",i,")",sep="",end=" ")
        print("  ",dt[f"st{i}"]["name"],dt[f"st{i}"]["price"],dt[f"st{i}"]["quantity"],sep=" => ")  

print()  

# => C) UPDATE PRODUCT INFORMATION : Allow the user to update the information (name,price,quantity) of an existing student by their specific id
print("________________________________________________________________________")   
print("                   UPDATE PRODUCT INFORMATION                           ")
print("________________________________________________________________________")

tot = int(input("Enter total product whose data you want to update : "))
i = 1
while i <= tot:
    rol = int(input("Enter id : "))
    fr = input(f"Enter what you to update (name,price,quantity) : ") 
    up = input(f"enter the new {fr} : ")
    if f"st{rol}" in dt:
        dt[f"st{rol}"][fr] = up
        i += 1
    else :
        print("enter valid id")


print("\nTHE DETAILS OF PRODUCT AFTER UPDATION ARE :- ")
print("=>ID.- Name - Price - Quantity  <=")
for i in range(1,n+1):
    check = 0
    for j in range(term):
        if i == lst[j] :  
             check = 1       
    if check == 0 :
        print(" ",i,")",sep="",end=" ")
        print("  ",dt[f"st{i}"]["name"],dt[f"st{i}"]["price"],dt[f"st{i}"]["quantity"],sep=" => ") 
print()    

# => D) SEARCH FOR A PRODUCT : Allow the user to search for a product by name or ID and display their details(ID,name,price,quantity)
print("________________________________________________________________________")   
print("                        SEARCH FOR A PRODUCT                            ")
print("________________________________________________________________________")

k = int(input("Enter total products you want to search : "))
for i in range(1,k+1):
    print(f"PRODUCT{i}:")
    search = input("Enter the id of the product you want to search : ")
    print("Name =>",dt[f"st{search}"]["name"])
    print("Price =>",dt[f"st{search}"]["price"])
    print("Quantity =>",dt[f"st{search}"]["quantity"])

# => E) DISPLAY ALL PRODUCT : Display all product in the inventory with their details
print("________________________________________________________________________")   
print("                         DISPLAY ALL PRODUCT                           ")
print("________________________________________________________________________")

print("\nTHE DETAILS OF ALL PRODUCTS :- ")
h = 1
for i in range(1,n+1):
    check = 0
    for j in range(len(lst)):
        if i == lst[j] :  
             check = 1       
    if check == 0 :
        print(f"{h})",end=" ")
        print("Name =>",dt[f"st{i}"]["name"])
        print("   Price =>",dt[f"st{i}"]["price"])
        print("   Quantity =>",dt[f"st{i}"]["quantity"])
        h += 1
   

""" Assignment done by VISHAL [Section - AF(2), Roll no. - 80] """