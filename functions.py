import mysql.connector as mys
cobj=mys.connect(host='localhost',user='root',passwd='Azsxdcfv1*',database='Library',auth_plugin='caching_sha2_password')
curob=cobj.cursor()

#For adding books
def addBook(x):
  for i in range (x):
    bkid=input('Enter the book id:')
    gre=input('Enter the genre of the book:')
    bkname=input('Enter the name of the book:')
    auth=input('Enter the author of the book:')
    copies=int(input('Enter the number of copies of the book:'))
    if f!=0:
      status=1
    else:
      status=0
    st="Insert into books values('{}','{}','{}','{}',{},{})".format(bkid,gre,bkname,auth,copies,status)
    curob.execute(st)
    cobj.commit() 

#for issuing books
def issueBook(y):
  for i in range(y):
    a=input('Enter the customer whose book has to be issued:')
    b=eval(input('Enter the book name/id you want to add'))
    curob.execute("select BOOK_ID, NAME from books")
    g=input('Enter the date in the form of yyyy-mm-dd.')
    d=curob.fetchall()
    c=''
    f=''
    if type(1)==type(b):
        c="Insert into issues values({},'{}','{}')".format(b,a,g)
    elif type('')==type(b):
        f=d[0][0]
        c="Insert into issues values({},'{}','{}')".format(f,a,g)
    curob.execute(c)
    cobj.commit()

def view_books(z):
  for i in range(z)
    try:
        curob.execute("SELECT * FROM books")
        books = curob.fetchall()
        if books:
            print("List of Books:")
            for book in books:
                print(f"Book ID: {book[0]}")
                print(f"Category: {book[1]}")
                print(f"Name: {book[2]}")
                print(f"Author: {book[3]}")
                print(f"Copies: {book[4]}")
                print(f"Status: {book[5]}")
                print("--------------------")
        else:
            print("No books found in the database.")
        cobj.close()

    except mys.Error as e:
        print(f"An error occurred: {str(e)}")

