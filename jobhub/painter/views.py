from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from painter import models
from painter.forms import NewPainter
# Create your views here.

def showList(request):
    employee = models.painter.objects.all()
    #username = request.session['username']
    res = render(request,'employee/employees.html',{'employee': employee,'category':'painter'})
    return res

def addList(request):
    form = NewPainter()
    res = render(request,'employee/new-employee.html',{'form':form,'category':'painter'})
    return res

def add(request):
    if request.method=='POST':
        form = NewPainter(request.POST)
        cp = models.painter()
        cp.name = form.data['name']
        cp.state = form.data['state']
        cp.dist = form.data['dist']
        cp.phone = form.data['phone']
        cp.pincode = form.data['pincode']
        cp.experience = form.data['experience']
        cp.fee = form.data['fee']
        cp.description = form.data['description']
        cp.save()
    s="record stored <br> <a href='/home/painter'>Go Back</a>"
    return HttpResponse(s)

def editList(request):
    employee = models.painter.objects.get(id=request.GET['id'])
    fields = {'name':employee.name,
        'state':employee.state,
        'dist':employee.dist,
        'phone':employee.phone,
        'pincode':employee.pincode,
        'experience':employee.experience,
        'fee':employee.fee,
        'description':employee.description
        }
    form = NewPainter(initial=fields)
    res = render(request,'employee/edit-list.html',{'form': form, 'employee': employee,'category':'painter'})
    return res

def edit(request):
    if request.method=='POST':
        form = NewPainter(request.POST)
        employee = models.painter()
        employee.id = request.POST['id']
        employee.name = form.data['name']
        employee.state = form.data['state']
        employee.dist = form.data['dist']
        employee.phone = form.data['phone']
        employee.pincode = form.data['pincode']
        employee.experience = form.data['experience']
        employee.fee = form.data['fee']
        employee.description = form.data['description']

        employee.save()
    s="record edited <br> <a href='/home/painter'>Go Back</a>"
    return HttpResponse(s)

def deleteList(request):
    employeeId = request.GET['id']
    employee = models.painter.objects.filter(id=employeeId)
    employee.delete()
    s="record deleted <br> <a href='/home/painter'>Go Back</a>"
    return HttpResponse(s)

def viewProfile(request):
    employeeId = request.GET['id']
    employee = models.painter.objects.get(id=employeeId)
    res = render(request,'painter/viewProfile.html',{'employee':employee})
    return res
