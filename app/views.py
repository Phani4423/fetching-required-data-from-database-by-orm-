from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models import Avg,Sum

# Create your views here.
def display(request):
    dnum = input('enter dept no : ')
    dname = input('enter dept name : ')
    dloc = input('enter djloc : ')
    TN = Dept.objects.get_or_create(dnum = dnum,dname = dname,dloc = dloc)
    if TN[0]:
        d = {'depts': Dept.objects.all()}
        return render(request,'display.html',d)
    else:
        return HttpResponse('already created')
def displayemp(request):
    enum = input('enter eept num : ')
    ename = input('enter eept name ')
    job = input('enter job : ')
    sal = input('enter sal : ')
    comm = input('enter comm : ')
    dnum = input('enter dnum : ')
    mgr = input('ente mgr : ')

    
    LOE = Dept.objects.filter(dnum = dnum)
    if LOE:
        TO =LOE[1]
        DN = Dept.objects.filter(dnum =TO,sal = sal,dname=ename,job = job,comm = comm ,enum = enum,mgr = mgr)
        d = {'employes':Emp.objects.all()}
        return render(request,'displayemp.html',d)
    else:
        return HttpResponse('alredy having')
def displayedata(request):
    employes = Emp.objects.filter(dnum = 20)
    d = {'employes': employes}
    return render(request,'displayemp.html',d)
        

        
    

def joints(request):
    LEDP = Emp.objects.select_related('dnum').filter(dnum__dname='RESEARCH')
    d = {'employes':LEDP}
    return render(request,'displayemp.html',d)
def prifix(request):
    LDTD = Dept.objects.prefetch_related('emp_set').all()
    d = {'LDTD':LDTD}
    return render(request,'prifix.html',d)
def empdept(request):
    print(Emp.objects.filter(dnum = 20).aggregate(Avg('sal')))
    return HttpResponse('created')
