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

def student_details(request):
    class_name=request.GET.get('class_name')
    
    if class_name:
        students=Students.objects.filter(class_name=class_name)
    else:
        students=Students.objects.all()
    classes=Students.objects.values('class_name').distinct()
    sections=Students.objects.values('section').distinct()
    context={
        'students':students,
        'classes':classes,
        'sections':sections
    }
    
    return render(request,'school/student_details.html',context)

def library(request,student_id):
    student=get_object_or_404(Students,student_id=student_id)
    book_records=library_records.objects.all()
    context={
        'student':student,
        'book_records':book_records
    }
    return render(request,'school/library.html',context)

def library_management(request,student_id,id):
    student=get_object_or_404(Students,student_id=student_id)
    book_records=get_object_or_404(library_records,book_id=id)
    if request.method=="POST":
        book_name=request.POST.get('book_name')
        author=request.POST.get('author')
        publication=request.POST.get('publication')
        edition=request.POST.get('edition')
        issued_date=request.POST.get('issued_date')
        return_date=request.POST.get('return_date')
        
        library_records.objects.create(
            book_name=book_name,
            author=author,
            publication=publication,
            edition=edition,
            issued_date=issued_date,
            return_date=return_date,
            
        )
        return redirect('library')
    context={
        'student':student,
        'book_records':book_records
    }
    return render(request,'school/library_management.html',context)
