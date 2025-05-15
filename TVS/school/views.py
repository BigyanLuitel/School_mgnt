from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.
def home(request):
    return render(request,'school/home.html')

def admission(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        class_name=request.POST.get('class_name')
        section=request.POST.get('section')
        contact=request.POST.get('contact')
        parents=request.POST.get('parents_name')
        address=request.POST.get('address')
        date_of_birth=request.POST.get('dob')
        date_of_admission=request.POST.get('dao')
        
        Students.objects.create(
            first_name=first_name,
            last_name=last_name,
            class_name=class_name,
            section=section,
            contact=contact,
            parents=parents,
            address=address,
            date_of_birth=date_of_birth,
            date_of_admission=date_of_admission
        )
    students=Students.objects.all()
    
    context={
        'students':students
    }
    return render(request,'school/admission.html',context)
def update_records(request,student_id):
    student=get_object_or_404(Students,student_id=student_id)
    if request.method=="POST":
        queryset=request.POST
        student.first_name=queryset.get('first_name')
        student.last_name=queryset.get('last_name')
        student.class_name=queryset.get('class_name')
        student.section=queryset.get('section')
        student.contact=queryset.get('contact')
        student.parents=queryset.get('parents_name')
        student.address=queryset.get('address')
        student.date_of_birth=queryset.get('dob')
        student.date_of_admission=queryset.get('dao')
        student.save()
        return redirect('admission')
    context={
        'student':student
    }
    return render(request,'school/update_records.html',context)

def delete_records(request,student_id):
    student=get_object_or_404(Students,student_id=student_id)
    if request.method=="POST":
        student.delete()
        return redirect('admission')  
    return redirect('admission')  

def student_details(request,student_id):
    student=get_object_or_404(Students,student_id=student_id)
    student=Students.objects.filter(class_name=student.class_name,section=student.section)
    context={
        'student':student
    }
    return render(request,'school/student_details.html',context)