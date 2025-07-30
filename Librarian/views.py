from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def student(request):
    return render(request,'student.html')
def faculty(request):
    return render(request,'faculty.html')
def librarian(request):
    return render(request,'librarian.html')
