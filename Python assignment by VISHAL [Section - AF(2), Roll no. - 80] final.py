""" PYHTON MINI PROJECT OR ASSIGNMENT GIVEN BY MAYANK SAXENA SIR  """

""" TOPIC -> Write a python a program that implements the student management system using dictionaries. The program should
             provide the following functionalities :
"""

print("************************************************************************")   
print("                             ADD A STUDENT                              ")
print("************************************************************************")   
# => A) ADD A STUDENT : Allow user to add a new student with a unique ID(or roll number),name,grade'

dt = {}

while True :
    n = input("Enter total students you want to add : ")
    count = 0
    for i in range(len(n)):
        if n[i] in "1234567890":
            count += 1
    if len(n) == count :
        break
    else :
        print("_ _ _ _ _ _ _ _ ")
        print(" INVALID NUMBER ")
        print("_ _ _ _ _ _ _ __")
n = int(n)
# code to get data of students from user 
for i in range(1,n+1):
    print(f"Enter details of student-{i} : ")
    a = input("Name -> ")
    b = input("Age -> ")
    c = input("Grade -> ")
    dt.update({f"st{i}":{"name":a,"age":b,"grade":c }})

# code to print the data of students provided by the user
print("\nTHE DETAILS OF STUDENTS ARE :- ")
print("=>Roll No.- Name - Age - Grade  <=")
for i in range(1,n+1):
    print(" ",i,")",sep="",end=" ")
    print("  ",dt[f"st{i}"]["name"],dt[f"st{i}"]["age"],dt[f"st{i}"]["grade"],sep=" => ")
print()    

print("------------------------------------------------------------------------\n")

print("************************************************************************")      
print("                           REMOVE A STUDENT                             ")
print("************************************************************************")   

# => B) REMOVE A STUDENT : Allow user to remove an existing student by specifying the student ID 

while True :
    while True :
        term = input("Enter total students whose details you want to delete : ")
        count = 0
        for i in range(len(term)) :
            if term[i] in "1234567890":
                count += 1
        if count == len(term):
            break
        else :
            print("_ _ _ _ _ _ _ _ ")
            print(" INVALID NUMBER ")
            print("_ _ _ _ _ _ _ __")                    
    
    if int(term) < n :
        break
    else :
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
        print("\"THE NUMBER YOU ENTERED IS MORE THAN THE TOTAL STUDENTS . ENTER A VALID NUMBER\" ") 
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
term = int(term)

lst = []     # in this we will store the roll number which we will delete
for i in range(1,term+1):
            while True :
                while True :
                    roll = input("Enter the roll number : ")
                    count = 0
                    for i in range(len(roll)):
                        if roll[i] in "1234567890":
                            count += 1
                    if count == len(roll):
                        break
                    else :
                        print("_ _ _ _ _ _ _ _ ")
                        print(" INVALID NUMBER ")
                        print("_ _ _ _ _ _ _ __")  
                roll = int(roll)
                if f"st{roll}" in dt :
                    break
                else : 
                    print("_ _ _ _ _ _ _ _ _ _")
                    print("INVALID ROLL NUMBER")
                    print("_ _ _ _ _ _ _ _ _ _")
            
            dt.pop(f"st{roll}")
            lst.append(roll)

# code to print the data of students after deleting some students data provided by the user
print("\nTHE DETAILS OF STUDENTS AFTER MODIFICATION ARE :- ")
for i in range(1,n+1):
    check = 0
    
    for j in range(term):
        if i == lst[j] : 
             check = 1       
    
    if check == 0 :
        print(" ",i,")",sep="",end=" ")
        print("  ",dt[f"st{i}"]["name"],dt[f"st{i}"]["age"],dt[f"st{i}"]["grade"],sep=" => ")  
print()  

print("------------------------------------------------------------------------\n")

print("************************************************************************")     
print("                   UPDATE STUDENT INFORMATION                           ")
print("************************************************************************")   
# => C) UPDATE STUDENT INFORMATION : Allow the user to update the information (name,age,grade) of an existing student by their specific id

while True : 
    while True : 
        tot = input("Enter total student whose data you want to update : ")
        count = 0
        for i in range(len(tot)):
            if tot[i] in "1234567890":
                count += 1
        if count == len(tot):
            break
        else :
            print("_ _ _ _ _ _ _ _ ")
            print(" INVALID NUMBER ")
            print("_ _ _ _ _ _ _ __") 

    if int(tot) <= (n - term):   # total student whose data is present are (n-term)
        break
    else :
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
        print("\"THE NUMBER YOU ENTERED IS MORE THAN THE TOTAL STUDENTS . ENTER A VALID NUMBER\" ") 
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
tot = int(tot)


# code to update students information
for i in range(tot) :
    while True :
        while True : 
            roll_no = input("Enter roll number : ")
            count = 0
            for i in range(len(roll_no)):
                if roll_no[i] in "1234567890":
                    count += 1
            if count == len(roll_no):
                roll_no = int(roll_no)
                break
            else :
                print("_ _ _ _ _ _ _ _ ")
                print(" INVALID NUMBER ")
                print("_ _ _ _ _ _ _ __")  
        
        if f"st{roll_no}" in dt :
            break
        else :
            print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
            print("INVALID ROLL NUMBER")
            print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    
    while True :
        fr = input(f"Enter what you want to update (name,age,grade) : ") 
        if fr == "name" or fr == "age" or fr == "grade":
            break
        else :
            print("_ _ _ _ _ _ _ _ _")
            print("INVALID OPERATION")
            print("_ _ _ _ _ _ _ _ _")

    up = input(f"Enter the new {fr} : ")

    if f"st{roll_no}" in dt:
        dt[f"st{roll_no}"][fr] = up
    else :
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
        print("=> ENTER VALID ROLL NUMBER <=")
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _")

# code to print the data of students after update the students information provided by the user
print("\nTHE DETAILS OF STUDENTS AFTER UPDATION ARE :- ")
print("=>Roll No.- Name - Age - Grade  <=")

for i in range(1,n+1):
    check = 0
    
    for j in range(term):
        if i == lst[j] :  
             check = 1       
    
    if check == 0 :
        print(" ",i,")",sep="",end=" ")
        print("  ",dt[f"st{i}"]["name"],dt[f"st{i}"]["age"],dt[f"st{i}"]["grade"],sep=" => ") 
print()    

print("------------------------------------------------------------------------\n")


print("************************************************************************")   
print("                        SEARCH FOR A STUDENT                            ")
print("************************************************************************")   
# => D) SEARCH FOR A STUDENT : Allow the user to search for a student by name or ID and display their details(ID,name,age,grade)

# code to search the students by their roll number (unique id)
while True :
    while True :
        k = input("Enter total students you want to search : ")
        count = 0
        for i in range(len(k)):
            if k[i] in "1234567890":
                count += 1
        if count == len(k):
            break
        else :
            print("_ _ _ _ _ _ _ _ ")
            print(" INVALID NUMBER ")
            print("_ _ _ _ _ _ _ __")                 
   
    if int(k) <= (n - term) :
        break
    else :
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
        print("\"THE NUMBER YOU ENTERED IS MORE THAN THE TOTAL STUDENTS . ENTER A VALID NUMBER\" ")
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
k = int(k)

for i in range(1,k+1):
    print(f"STUDENT{i}:")
    while True :
        search = input("Enter the roll number of the student you want to search : ")
        
        if f"st{search}" in dt :
            break
        else :
            print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
            print("=> ENTER VALID ROLL NUMBER <=")
            print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _")   

    print("Name =>",dt[f"st{search}"]["name"])
    print("Age =>",dt[f"st{search}"]["age"])
    print("Grade =>",dt[f"st{search}"]["grade"])
print()

print("------------------------------------------------------------------------\n")

print("************************************************************************")   
print("                         DISPLAY ALL STUDENT                            ")
print("************************************************************************")   

# => E) DISPLAY ALL STUDENT : Display all students in the school with their details

print("TO DISPLAY ALL THE REMAINING STUDENTS DATA, ENTER '1' , if don't want press enter \n")
ch = input("Enter : ")

if ch == "1" :
    print("\nTHE DETAILS OF ALL STUDENTS :- ")
    h = 1
    for i in range(1,n+1):
        check = 0
        
        for j in range(len(lst)):
            if i == lst[j] :  
                 check = 1       
        
        if check == 0 :
            print(f"{h})",end=" ")
            print("Name =>",dt[f"st{i}"]["name"])
            print("   Age =>",dt[f"st{i}"]["age"])
            print("   Grade =>",dt[f"st{i}"]["grade"])
            h += 1
else :
    pass   
print("\n**************************************")   
print("THANK YOU \nPROGRAM RUNS SUCCESFULLY")
print("**************************************")   

""" Assignment done by VISHAL [Section - AF(2) , Cls Roll no. - 80 ] """

#---------------------------------------- THANK YOU --------------------------------------------------------#