from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from electrician import models
from electrician.forms import NewEc
# Create your views here.

def showList(request):
    employee = models.electrician.objects.all()
    #username = request.session['username']
    res = render(request,'employee/employees.html',{'employee': employee,'category':'electrician'})
    return res

def addList(request):
    form = NewEc()
    res = render(request,'employee/new-employee.html',{'form':form,'category':'electrician'})
    return res

def add(request):
    if request.method=='POST':
        form = NewEc(request.POST)
        cp = models.electrician()
        cp.name = form.data['name']
        cp.state = form.data['state']
        cp.dist = form.data['dist']
        cp.phone = form.data['phone']
        cp.pincode = form.data['pincode']
        cp.experience = form.data['experience']
        cp.fee = form.data['fee']

        cp.save()
    s="record stored <br> <a href='/home/electrician'>Go Back</a>"
    return HttpResponse(s)

def editList(request):
    employee = models.electrician.objects.get(id=request.GET['id'])
    fields = {'name':employee.name,
        'state':employee.state,
        'dist':employee.dist,
        'phone':employee.phone,
        'pincode':employee.pincode,
        'experience':employee.experience,
        'fee':employee.fee
        }
    form = NewEc(initial=fields)
    res = render(request,'employee/edit-list.html',{'form': form, 'employee': employee,'category':'electrician'})
    return res

def edit(request):
    if request.method=='POST':
        form = NewEc(request.POST)
        employee = models.electrician()
        employee.id = request.POST['id']
        employee.name = form.data['name']
        employee.state = form.data['state']
        employee.dist = form.data['dist']
        employee.phone = form.data['phone']
        employee.pincode = form.data['pincode']
        employee.experience = form.data['experience']
        employee.fee = form.data['fee']

        employee.save()
    s="record edited <br> <a href='/home/electrician'>Go Back</a>"
    return HttpResponse(s)

def deleteList(request):
    employeeId = request.GET['id']
    employee = models.electrician.objects.filter(id=employeeId)
    employee.delete()
    s="record deleted <br> <a href='/home/electrician'>Go Back</a>"
    return HttpResponse(s)

def viewProfile(request):
    employeeId = request.GET['id']
    employee = models.electrician.objects.get(id=employeeId)
    res = render(request,'electrician/viewProfile.html',{'employee':employee})
    return res
