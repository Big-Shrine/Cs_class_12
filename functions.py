import anvil.server
import mysql.connector as mys
from datetime import datetime

anvil.server.connect("server_ZKVLF6KO2J263VRFCP6XAVDD-7GVA2356LSL76HX5")
cobj=mys.connect(host='localhost',user='root',passwd='Azsxdcfv1*',database='Library',auth_plugin='caching_sha2_password')
curob=cobj.cursor()

#for executing sql commands
def executor(h):
  curob.execute(h)
  cobj.commit()
  
#function for issuing book
@anvil.server.callable
def issueBooks(customer, bookid, datetime_str):
    curob.execute("select BOOK_ID, NAME, COPIES, STATUS from books")
    books = curob.fetchall()
    message = ''

    try:
        if datetime_str:
            datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
        else:
            datetime_obj = None

        for i in books:
            if bookid in i:
                l = i[2] - 1
                if l==0:
                    status = f"update books set COPIES={str(l)}, STATUS=0 where BOOK_ID='{i[0]}'"
                    executor(status)
                    message = "Book issued successfully"
                    break
                elif l == -1:
                    message = 'Book unavailable'
                    break
                else:
                    status = f"update books set COPIES={str(l)} where BOOK_ID='{i[0]}'"
                    executor(status)
                    message = "Book issued successfully"
                    break 
        else:
              message = 'Invalid book ID'
              
        curob.execute("select customer_id,books_issued from customer_details")
        h = curob.fetchall()
        for i in h:
            if customer in i:
                issued = f"update customer_details set books_issued={str(i[1]+1)} where customer_id='{str(i[0])}'"
                executor(issued)
                break
        else:
            message = 'Invalid customer ID'

              
        if message != 'Book unavailable' and message != 'Invalid book ID' and message != 'Invalid customer ID':
                if datetime_str:
                    c = f"Insert into book_issues(customer_id, book_id, date_of_issue) values('{customer}','{bookid}','{datetime_str}')"
                else:
                    c = f"Insert into book_issues(customer_id, book_id) values('{customer}','{bookid}')"
                executor(c)
                
    except ValueError:
        message = 'Invalid datetime format. Please enter the datetime in the format YYYY-MM-DD HH:MM:SS'

    return message

#For adding books
@anvil.server.callable
def addBook(bkid, gre, bkname, auth, copies):
    try:
        c=0
        curob.execute('select BOOK_ID from books')
        d=curob.fetchall()
        for i in d:
            check=i[0]
            if bkid in check:
                raise ValueError('Book ID already in use')
        
        else:
            if not (isinstance(bkid, str) and len(bkid)== 5 and bkid[:2].isalpha() and bkid[2:].isdigit() and bkid[:2].isupper()):
                raise ValueError("Invalid format for Book ID. It should be two capital letters followed by 3 numbers.")
        
            if type(copies)==type(c) and copies!=0:
                status=1
            elif type(copies)==type(c) and copies==0:
                status=0
            else:
                raise ValueError("Copies field has to be a number")
        
        
        st="Insert into books values('{}','{}','{}','{}',{},{})".format(bkid,gre,bkname,auth,copies,status)
        executor(st)
        message = "Book added successfully"
        return message
      
    except ValueError as e:
        message = str(e)
        return message


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

