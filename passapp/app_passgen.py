import psycopg2


def sinup():
        try:
                username = str(input("enter your username:"))
                password = str(input("enter your password"))
                commond = """CREATE TABLE {hello} (about VARCHAR, something VARCHAR)""".format(hello = username)
                commond_update = """ INSERT INTO {create1} (about, something) VALUES ('{username1}', '{password1}')""".format(create1=username, username1= username, password1= password)
                cursor.execute(commond)
                cursor.execute(commond_update)
                conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
                print(error)
def login():
        try:
                username = input("enter your username:")
                password = input("Enter your password:")
                commond = """ SELECT about,something FROM {tb}""".format(tb =username )
                cursor.execute(commond)
                records = [row for row in cursor.fetchall()]
                user = records[0]
                if(username == user[0] and password == user[1]):
                        print("logged in successfully")
                else:
                        print("incorrect password or username:")

        except psycopg2.errors.UndefinedTable:
                print("You are not registered please sinup")
                print("redirecting to sinup \n please singup here")
                sinup()
conn = psycopg2.connect(database="postgres", user='postgres', password='pass123', host='127.0.0.1', port= '5432')

cursor = conn.cursor()
option  = int(input("enter your option: \n 1 for login\n 2 for sinup "))
if (option== 1):
        login()
elif(option == 2):
        sinup()
conn.close()