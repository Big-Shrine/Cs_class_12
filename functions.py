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


def view_books():
  try:
    curob.execute("SELECT BOOK_ID, CATEGORY, NAME, AUTHOR, COPIES, IF(STATUS=1,'AVAILABLE','NOT AVAILABLE') FROM books")
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
  except mys.Error as e:
    print(f"An error occurred: {str(e)}")

