from django.shortcuts import render
import pymysql

# Create your views here.
def home(request):
    return render(request,'home.html',)
def student(request):
    return render(request,'student.html')
def studentregister(request):
      return render(request,"studentregister.html")
def StudentRegAction(request):
    n=request.POST['name']
    g=request.POST['gender']
    l=request.POST['lang']
    y=request.POST['year']
    u=request.POST['username']
    p=request.POST['password']
    con=pymysql.connect(host="localhost", user="root", password="lucky", database="lib2")
    cur=con.cursor()
    i=cur.execute("insert into studentregister values('"+n+"','"+g+"','"+l+"','"+y+"','"+u+"','"+p+"')")
    con.commit()
    if i>0:
        context={'data':'Registration sucessful'}
        return render(request,"studentregister.html",context)
    else:
        context={'data':'Registration Failed'}
        return render(request,"studentregister.html",context) 

def StudentLogAction(request):
    u=request.POST["username"]
    p=request.POST["password"]
    con=pymysql.connect(host="localhost",user="root",password="root",database="libman")
    cur=con.cursor()
    i=cur.execute("select * from register where username='"+u+' and password="'+p+"' ")                    
    if i>0:
       return render(request,"Studenthome.html")
    else:
        context={'data':'login Failed....'}
def faculty(request):
    return render(request,'faculty.html')
def librarian(request):
    return render(request,'librarian.html')


