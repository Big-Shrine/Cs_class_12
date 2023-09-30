import mysql.connector as mys
cobj=mys.connect('local host','root','Azsxdcfv1*','Library')
curob=cobj.cursor()
def addBook(x):
  #x=input("Enter the number of books you want to add")
  for i in range (x):
    b=input('Enter the book id')
    c=input('Enter the genre of the book')
    d=input('Enter the name of the book')
    e=input('Enter the author of the book')
    f=int(input('Enter the number of copies of the book'))
    if f!=0:
      g=0
    else:
      g=1
    st="Insert into books values('{}','{}','{}','{}',{},{})".format(b,c,d,e,f,g)
    curob.execute(st)
    curob.commit()
      
    
