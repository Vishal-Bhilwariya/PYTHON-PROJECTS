# add a contact
print("ADD A CONTACT")
a = int(input("enter total contact number => "))

dt = {}
for i in range(a):
    print(f"DETAIL-{i+1} :-")
    b = input("Enter name => ")
    c = input("Enter mobile number => ")
    dt.update({f"st{i+1}" : {"name":b,"contact" : c}})

for i in range(a):
    print(i+1,")",end=" ")
    print("NAME -> ",dt[f"st{i+1}"]["name"])    
    print("  CONTACT -> ",dt[f"st{i+1}"]["contact"])  

# remove a contact

print("REMOVE A CONTACT")
lst = []
d = int(input("enter total contact to delete =>  "))
for i in range(d):
    e = int(input(("Enter id => ")))
    dt.pop(f"st{e}")
    lst.append(e)      

for i in range(a):
    check = 0
    for j in range(len(lst)):
        if i+1 == lst[j]:
            check = 1
    if check == 0 :
        print(i+1,")",end=" ")
        print("NAME -> ",dt[f"st{i+1}"]["name"])    
        print("  CONTACT -> ",dt[f"st{i+1}"]["contact"])  

# search for a contact
print("SEARCH A CONTACT")
f = int(input("Enter total contact to be searched => "))

for i in range(f):
    g = int(input("enter id => "))
    print(i+1,")",dt[f"st{g}"]["name"],"\n ",dt[f"st{g}"]["contact"])

# display all student    

print("ALL CONATCTS")
for i in range(a):
    check = 0
    for j in range(len(lst)):
        if i+1 == lst[j]:
            check = 1
    if check == 0:
        print(i+1,")",end=" ")
        print("NAME -> ",dt[f"st{i+1}"]["name"])    
        print("  CONTACT -> ",dt[f"st{i+1}"]["contact"]) 