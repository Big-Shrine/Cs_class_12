import mysql.connector as mys
cobj=mys.connect(host='localhost',user='root',passwd='Azsxdcfv1*',database='Library',auth_plugin='caching_sha2_password')
curob=cobj.cursor()

#for executing sql commands
def executor(h):
  curob.execute(h)
  cobj.commit()

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
    executor(st) 

#for issuing books
def issueBooks(y):
  for i in range(y):
    customer=input('Enter the customer-ID whose book has to be issued:')
    bookid=input('Enter the ID of the book you want to add:')
    curob.execute("select BOOK_ID, NAME, COPIES, STATUS from books")
    books=curob.fetchall()
    flag=False
    for i in books:
      if bookid in i:
        flag=True
        l=i[2]-1
        if l==0:
          status=f"update books set COPIES={str(l)}, STATUS=0 where BOOK_ID={i[0]}"
          executor(status)
        elif l==-1:
          print('Book not available')
          continue
        else:
          status=f"update books set COPIES={str(l)} where BOOK_ID={i[0]}"
          executor(status)
        datetime=input('Enter the date and time of issue in the form of YYYY-MM-DD HH:MM:SS or click enter to add current date and time:')
        print('---------------------------------------')
        if datetime:
          c=f"Insert into book_issues(customer_id, book_id, date_of_issue) values({customer},{bookid},'{datetime}')"
        else:
          c=f"Insert into book_issues(customer_id, book_id) values({customer},{bookid})"
        executor(c)
        curob.execute("select customer_id,books_issued from customer_details")
        h=curob.fetchall()
        for i in h:
          if customer in i:
            issued=f"update customer_details set books_issued={str(i[1]+1)} where customer_id={i[0]}"
            executor(issued)
        break
    if not flag:
      print('Book not found')
      print('---------------------------------------')

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

