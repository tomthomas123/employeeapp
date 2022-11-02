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
        empcode =input("Enter the empcode  : ")
        empname = input("enter the name : ")
        
        designation = input("Enter the designation : ")
        salary =input("Enter the salary : ")
        cmpname = input("Enter the company name : ")
        phone = input("Enter the phone number  : ")
        emailid = input("enter the emailid  : ")
        password = input("Enter the password : ")
        sql = 'INSERT INTO `employee`(`empcode`, `empname`, `designation`, `salary`, `companyname`, `phone`, `emailid`, `password`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
        data = (empcode,empname,designation,salary,cmpname,phone,emailid,password)
        mycursor.execute(sql,data)
        mydatabase.commit()
    elif choice==2:
        print("view all employee selected ")
        sql = 'SELECT * FROM `employee` ' 
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(result)
    elif choice==3:
        print("search the  employee  ")
        empcode = input("Enter the employee code to be search : ")
        sql = "SELECT `empname`, `designation`, `salary`, `companyname`, `phone`, `emailid`, `password` FROM `employee` WHERE `empcode` = " +empcode
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)
    elif choice==4:
        print("update the employee  ")
        empcode = input("Enter the employee code ")
        name = input("Enter the name to be add : ")
        designation = input("Enter the designation to be add : ")
        salary = input("Ënter the salary to be updated : ")
        companyname = input("Enter the company name to be update : ")
        phone = input("Enter the phone to be update : ")
        emailid = input("Enter the email id to be update : ")
        password = input("Enter the password to be updated : ")
        sql = "UPDATE `employee` SET `empname`='"+name+"',`designation`='"+designation+"',`salary`='"+salary+"',`companyname`='"+companyname+"',`phone`='"+phone+"',`emailid`='"+emailid+"',`password`='"+password+"' WHERE `empcode`=" +empcode
        mycursor.execute(sql)
        result =mycursor.fetchall()
        mydatabase.commit()
        print(f"{empcode}'s data updated successfully") 
    elif choice==5:
        print("delete the employee  ")
    elif choice==6:
        break
