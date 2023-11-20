import sqlite3

conn = sqlite3.connect("Assignment.db")

"""
conn.execute('''CREATE TABLE Teacher(
             t_id VARCHAR(50) PRIMARY KEY,
             name VARCHAR(50) NOT NULL,
            salary INT NOT NULL
)''')
conn.commit()

conn.execute('''INSERT INTO Teacher (t_id,name,salary) VALUES ("t_1","abc",50000), 
             ("t_2","def",60000),
             ("t_3","xyz",40000),
             ("t_4","hgf",35000),
             ("t_5","jig",65000)
''')
conn.commit()

conn.execute('''CREATE TABLE Student(
             s_id VARCHAR(50) PRIMARY KEY,
             cgpa DECIMAL(10,2) NOT NULL,
             name VARCHAR(50) NOT NULL,
             t_id VARCHAR(50) NOT NULL,
             FOREIGN KEY(t_id) REFERENCES Teacher(t_id)
)''')
conn.commit()

conn.execute('''INSERT INTO Student(s_id,cgpa,name,t_id) VALUES ("s_1",9.0,"abc","t_1"),
             ("s_2",8.5,"def","t_1"),
             ("s_3",9.5,"ghi","t_2"),
             ("s_4",7.0,"hijk","t_4"),
             ("s_5",10.0,"fig","t_5")
''')
conn.commit()


conn.execute('''CREATE TABLE Dept(
             d_id VARCHAR(50) PRIMARY KEY,
             name VARCHAR(50) NOT NULL
)''')

conn.commit()


conn.execute('''INSERT INTO Dept(d_id,name) VALUES("d_1","CSE"),
             ("d_2","ECE"),
             ("d_3","EEE")
''')
conn.commit()



conn.execute('''CREATE TABLE Part(
             t_id VARCHAR(50) ,
             d_id VARCHAR(50) ,
             PRIMARY KEY (t_id,d_id),
             FOREIGN KEY (t_id) REFERENCES Teacher(t_id),
             FOREIGN KEY (d_id) REFERENCES Dept(d_id)
)''')
conn.commit()



conn.execute('''INSERT INTO Part(t_id,d_id) VALUES ("t_1","d_1"),
             ("t_2","d_2"),
             ("t_3","d_1"),
             ("t_4","d_2"),
             ("t_5","d_3")
''')
conn.commit()
"""

cursor = conn.execute(''' SELECT * FROM Student WHERE cgpa > 8.0''')
for row in cursor:
    print(row)
print("-----------------------------")

cursor = conn.execute('''SELECT * FROM Teacher WHERE salary > 50000''')
for row in cursor:
    print(row)
print("-----------------------------")

cursor = conn.execute('''SELECT * FROM Student JOIN Teacher ON Student.t_id = Teacher.t_id;''')
for row in cursor:
    print(row)
print("-----------------------------")

cursor = conn.execute('''SELECT * FROM Teacher 
                      JOIN Part ON Teacher.t_id = Part.t_id
                      JOIN Dept ON Part.d_id = Dept.d_id''')
for row in cursor:
    print(row)
print("-----------------------------")

cursor = conn.execute('''SELECT s_id,Student.name,Dept.name FROM Student 
                      JOIN Teacher ON Teacher.t_id = Student.t_id 
                      JOIN Part ON Teacher.t_id = Part.t_id
                      JOIN Dept ON Part.d_id = Dept.d_id''')
for row in cursor:
    print(row)
print("-----------------------------")