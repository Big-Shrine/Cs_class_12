import mysql.connector as mys
cobj=mys.connect(host='localhost',user='root',passwd='Azsxdcfv1*',database='Library',auth_plugin='caching_sha2_password')
curob=cobj.cursor()
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
def issueBook(y):
  for i in range(y):
    a=input('Enter the customer whose book has to be issued:')
    b=eval(input('Enter the book name/id you want to add'))
    if type(1)==type(b):
      
