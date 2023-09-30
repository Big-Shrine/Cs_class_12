import mysql.connector as mys
cobj=mys.connect(host='localhost',user='root',passwd='Azsxdcfv1*',database='Library',auth_plugin='caching_sha2_password')
curob=cobj.cursor()
def addBook(x):
  for i in range (x):
    b=input('Enter the book id')
    c=input('Enter the genre of the book')
    d=input('Enter the name of the book')
    e=input('Enter the author of the book')
    f=int(input('Enter the number of copies of the book'))
    if f!=0:
      g=1
    else:
      g=0
    st="Insert into books values('{}','{}','{}','{}',{},{})".format(b,c,d,e,f,g)
    curob.execute(st)
    cobj.commit()
      
    
