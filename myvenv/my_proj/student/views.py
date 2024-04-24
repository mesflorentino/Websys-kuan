from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def stud(request):
    template = "create.html"
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid:
            try:
                form.save()
                return redirect('/')
            
            except:
                pass
            
    else:
        form = StudentForm()
        
    context = {
        "form": form
    }
        
    return render(request, template, context)
    
def show(request):
    template = "show.html"
    students = Student.objects.all()
    context = {
        "students": students
    }
    return render(request, template, context)

def edit(request, id):
    template = "edit.html"
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    context = {
        "form": form,
        "student": student
    }
    return render(request, template, context)

def update(request, id):
    template = "edit.html"
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST, instance = student)
    if form.is_valid:
        form.save()
        return redirect("/")
    context = {
        "student": student
    }
    
    return render(request, template, context)

def destroy(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("/")