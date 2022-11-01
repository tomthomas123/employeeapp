import mysql.connector

mydatabase = mysql.connector.connect(host = 'localhost',user = 'root' ,password = '',database = 'employeedb')

mycursor = mydatabase.cursor()
while True:
    print(" Enter your option")
    print("""             1. add employee
             2. view all employee
             3. search a employee
             4. update the employee
             5. delete a employee
             6. exit   
              """)   
    choice = int(input("Enter your option : "))
    if choice==1:
        print("employee entry selected")
        
    elif choice==2:
        print("view all employee selected ")
    elif choice==3:
        print("search the  employee  ")
    elif choice==4:
        print("update the employee  ")
    elif choice==5:
        print("delete the employee  ")
    elif choice==6:
        break
