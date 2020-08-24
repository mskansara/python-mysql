import mysql.connector

#Open database connection
db = mysql.connector.connect(host = "localhost", user = "root", password = "root", database = "studentsdb")

cursor = db.cursor(buffered=True)

if not cursor:
    print("No table")
    cursor.execute("CREATE TABLE students (student_id VARCHAR(20) PRIMARY KEY, student_name VARCHAR(128), gender VARCHAR(10), email_id VARCHAR(128) UNIQUE)")

print("---------Students Directory---------")

choice = int(input("Choose an option:\n1. Add Student\n2.Search Student\n3.Display Students\n"))

if choice == 1:
    student_id = input("Student ID: ")
    student_name = input("Student Name: ")
    gender = input("Gender: ")
    email = input("Email ID: ")

    sql = "INSERT INTO students (student_id, student_name, gender, email_id) VALUES(%s, %s, %s, %s)"
    val = (student_id, student_name, gender, email)

    cursor.execute(sql, val)
    db.commit()

    print(cursor.rowcount, "record inserted")

elif choice == 2:
    s_id = input("Enter Student Id: ")
    sql = "SELECT * FROM students WHERE student_id = %s"
    val = (s_id,)
    cursor.execute(sql,val)
    result = cursor.fetchone()
    if result:
        
        print("Student ID: ",result[0],"\nStudent Name: ",result[1],"\nGender: ",result[2],"\nEmail Id: ",result[3])
    else:
        print("Error: No records found")

elif choice == 3:
    sql = "SELECT * FROM students"
    cursor.execute(sql)
    result = cursor.fetchall()
    
    print("Student ID\tStudent Name\tGender\tEmail Id")
    for row in result:
        print("\t",row[0],"    ",row[1],row[2],"  ",row[3])

else: 
    print("Error")


# print(student_id,"\n",student_name,"\n",gender,"\n",email)