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
def addBook(gre, bkname, auth, copies):
    try:        
        if copies.isdigit() and int(copies)!=0:
            status=1
        elif copies.isdigit() and int(copies)==0:
            status=0
        else:
            raise ValueError("Copies field has to be a number")
        
        
        intcopy=int(copies)
        st="Insert into books (CATEGORY, NAME, AUTHOR, COPIES, STATUS) values('{}','{}','{}',{},{})".format(gre,bkname,auth,intcopy,status)
        executor(st)
        message = "Book added successfully"
        return message
      
    except ValueError as e:
        message = str(e)
        return message


#for viewing books
@anvil.server.callable 
def view_books():
  curob2=cobj.cursor(dictionary=True)
  curob2.execute("SELECT BOOK_ID, CATEGORY, NAME, AUTHOR, COPIES, IF(STATUS=1,'AVAILABLE','NOT AVAILABLE') as STATUS FROM books")
  books = curob2.fetchall()
  
  if books:
      return books
  else:
      message= "No books in the system."
      return message
