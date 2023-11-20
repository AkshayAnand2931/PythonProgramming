"""
class myexception(Exception):
    
    def __init__(self,str1):
        self.str = str1

    def __str__(self):
        return self.str
    
n = int(input("Enter the value of n: "))

try:
    if not 1 <= n <= 100:
        raise myexception("Not in range.")
    else:
        print("its a valid number.")

except myexception as e:
    print(e)

--------------------------------------------------------------------------------------------------------------------------

class mydate:
    
    def __init__(self,dd,mm,yy):
        self.dd = dd
        self.mm = mm
        self.yy = yy
    
    def __str__(self) -> str:
        return str(self.dd) + "-" + str(self.mm) + "-" + str(self.yy)
    

class myevent:
    
    def __init__(self,dd,mm,yy,detail):
        self.date = mydate (dd,mm,yy) #object creation for mydate
        self.detail = detail

    def __str__(self) -> str:
        return str(self.date) + "===>" + str(self.detail)
    
e = myevent(3,7,2023,"PAP Course")
print(e)

------------------------------------------------------------------------------------------------------------------------------


memory = {}

def memoize_function(f):

    def inner(num):
        if num not in memory:
            memory[num] = f[num]
        else:
            print("returning result fro storedn memory")
            return memory[num]
        return inner

@memoize_function
def facto(num):
    if num == 1:
        return 1
    else 
        return num * facto(num - 1)

--------------------------------------------------------------------------------------------------------------------------

class singleton:

    _instance = None

    def __new__(cls):
        if cls.isinstance == None:
            print("creating objects")
            cls._instance = super().__new__(cls)

        return cls._instance
    
ob1 = singleton()
print(ob1)
ob2 = singleton()
print(ob2)

---------------------------------------------------------------------------------------------------------------------------------


#Observer design pattern

class Publisher:

    def __init__(self):
        pass

    def register(self):
        pass

    def unregister(self):
        pass

    def notifyAll(self):
        pass

class TechForum(Publisher):

    def __init__(self):
        self._listofusers = []
        self.postname = None
    
    def register(self,userObj):
        if  userObj not in self._listofusers:
            self._listofusers.append(userObj)

    def unregister(self,userObj):
        self._listofusers.remove(userObj)

    def notifyAll(self):
        for obj in self._listofusers:
            obj.notify(self.postname)

    def writeNewPost(self,postname):
        self.postname = postname
        self.notifyAll()

class Subscriber:

    def __init__(self):
        pass
    def notify(self):
        pass

class User1(Subscriber):

    def notify(self,postname):
        print("User 1 is notified of post %s"%postname)

class User2(Subscriber):

    def notify(self,postname):
        print("User 2 is notified of post %s"%postname)

if __name__ == "__main__":

    techforum = TechForum()
    user1 = User1()
    user2 = User2()

    techforum.register(user1)
    techforum.register(user2)

    techforum.writeNewPost("Hello there.")
    techforum.unregister(user2)
    techforum.writeNewPost("General Kenobi.")

----------------------------------------------------------------------------------------------------------------------------------


class EnglishSpeaker:
    
    def responseToGreeting(self):
        return "Hello to you too"
    
class Translator:
    englishToFrenchPhrases = {"Hello to you too" : "Bonjour a vous aussi"}

    def __init__(self,englishSpeaker):
        self.englishSpeaker = englishSpeaker

class FrenchSpeaker:

    def __init__(self,englishToFrenchTranslator):
        self.englishToFrenchTranslator = englishToFrenchTranslator

    def exchange_greeting(self):
        print(self.englishToFrenchTranslator.englishToFrenchPhrases[self.englishToFrenchTranslator.englishSpeaker])

if __name__ == "__main__":

    englishSpeaker = EnglishSpeaker()
    englishToFrenchTranslator = Translator(englishSpeaker)
    frenchSpeaker = FrenchSpeaker(englishToFrenchTranslator)
    frenchSpeaker.exchange_greeting()

-------------------------------------------------------------------------------------------------------------------------------


import re

pattern = "this"
text = "this is a pap class"

match = re.search(pattern,text)
print(match.start())
print(match.end())

s = "geeks for geeks"
match = re.search(".",s)
print(match)

string = "this is easy programming language"
pattern = "[a-m]"
pattern2 = "^[a-m]"
pattern3 = "[a-m]$"

match = re.findall(pattern,string)
print(match)

txt = "the rain in spain"
x = re.findall("\brain",txt)
y = re.findall("\bthe",txt)
print(x)


text = "this is python and this is regular expression"
pattern = "this"
t = re.finditer(pattern,text)
for i in t:
    print(i)

text = "python programming"
pattern = "python program"
print(re.fullmatch(pattern,text))

text = "this is find and replace kind of function"
pattern = "f"
repl = "F"
print(re.sub(pattern,repl,text))

---
--------------------------------------------------------------------------------------------------------------


import sqlite3

sqliteConnection = sqlite3.connect("sql.db")
cursor = sqliteConnection.cursor()
print("Database connected.")

query = '''SELECT sqlite_version();'''
cursor.execute(query)

result = cursor.fetchall()
print(result)

------------------------------------------------------------------------------------------------------------------


import sqlite3

conn = sqlite3.connect('sql.db')

#cursor.execute('''CREATE TABLE salesman2 (salesman_id INT(5),name CHAR(50),city CHAR(50),commission CHAR(50));''')

s_id = int(input("salesman id: "))
s_name =  input("salesman name: ")
s_city = input("salesman city: ")
s_comm = input("salesman commission: ")

conn.execute('''INSERT INTO salesman2 (salesman_id,name,city,commission) VALUES (?,?,?,?);''',(s_id,s_name,s_city,s_comm))
conn.commit()

cursor = conn.execute('''SELECT * FROM salesman2;''')

for row in cursor:
    print(row)

conn.commit()

print("Data entered successfully.")

conn.close()

----------------------------------------------------------------------------------------------------------------------
"""

