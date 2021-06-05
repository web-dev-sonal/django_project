from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from teacher import models
from teacher.forms import NewTeacher
# Create your views here.

def showList(request):
    employee = models.teacher.objects.all()
    #username = request.session['username']
    res = render(request,'employee/employees.html',{'employee': employee,'category':'teacher'})
    return res

def addList(request):
    form = NewTeacher()
    res = render(request,'employee/new-employee.html',{'form':form,'category':'teacher'})
    return res

def add(request):
    if request.method=='POST':
        form = NewTeacher(request.POST)
        cp = models.teacher()
        cp.name = form.data['name']
        cp.state = form.data['state']
        cp.dist = form.data['dist']
        cp.phone = form.data['phone']
        cp.pincode = form.data['pincode']
        cp.experience = form.data['experience']
        cp.fee = form.data['fee']
        cp.description = form.data['description']
        cp.subject = form.data['subject']
        cp.email = form.data['email']

        cp.save()
    s="record stored <br> <a href='/home/teacher'>Go Back</a>"
    return HttpResponse(s)

def editList(request):
    employee = models.teacher.objects.get(id=request.GET['id'])
    fields = {'name':employee.name,
        'state':employee.state,
        'dist':employee.dist,
        'phone':employee.phone,
        'pincode':employee.pincode,
        'experience':employee.experience,
        'fee':employee.fee,
        'description':employee.description,
        'email':employee.email,
        'subject':employee.subject
        }
    form = NewTeacher(initial=fields)
    res = render(request,'employee/edit-list.html',{'form': form, 'employee': employee,'category':'teacher'})
    return res

def edit(request):
    if request.method=='POST':
        form = NewTeacher(request.POST)
        employee = models.teacher()
        employee.id = request.POST['id']
        employee.name = form.data['name']
        employee.state = form.data['state']
        employee.dist = form.data['dist']
        employee.phone = form.data['phone']
        employee.pincode = form.data['pincode']
        employee.experience = form.data['experience']
        employee.fee = form.data['fee']
        employee.description = form.data['description']
        employee.email = form.data['email']
        employee.subject = form.data['subject']

        employee.save()
    s="record edited <br> <a href='/home/teacher'>Go Back</a>"
    return HttpResponse(s)

def deleteList(request):
    employeeId = request.GET['id']
    employee = models.teacher.objects.filter(id=employeeId)
    employee.delete()
    s="record deleted <br> <a href='/home/teacher'>Go Back</a>"
    return HttpResponse(s)

def viewProfile(request):
    employeeId = request.GET['id']
    employee = models.teacher.objects.get(id=employeeId)
    res = render(request,'teacher/viewProfile.html',{'employee':employee})
    return res
