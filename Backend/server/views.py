from audioop import reverse
import datetime
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *

#Signup Page Rendering
def signup(request):
    return render(request,"signup.html")

#Storing User Details
def register(request):
    if request.method=='POST':
        fname=request.POST.get('firstName')
        lname=request.POST.get('lastName')
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        zip=request.POST.get('zip')
        print("USERNAME IS "+username+" AND PASSWORD IS "+password)
        user=Details(fname=fname,lname=lname,username=username,password=password,email=email,contact=contact,zip=zip)
        user.save()
        messages.success(request,"Your Account Has Been Created Successfully")
        return redirect("/login")


def disp(request,pid,did):
    doc=Doctors.objects.filter(docid=did)
    return render(request,"display.html",{
        "users":doc,
        "pid":pid
    })


#Rendering Admin Home Page
def admhome(request):
    return render(request,"admin.html")

#Rendering Add Doctor page
def addoc(request):
    return render(request,"newdoc.html")

#Storing Doctor Data
def storedoc(request):
    if request.method=='POST':
        name=request.POST.get('name')
        spl=request.POST.get('specialisation')
        password=request.POST.get('password')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        addrs=request.POST.get('address')
        print("USERNAME IS "+email+" AND PASSWORD IS "+password)
        user=Doctors(docname=name,specialisation=spl,password=password,docemail=email,contact=contact,address=addrs)
        user.save()
        messages.success(request,"Doctor Has Been Added Successfully")
        return redirect("/getdoc")

#Rendering Doctors Display Page - Admin
def getdoc(request):
    docs=Doctors.objects.all()
    if docs:
        return render(request,"admdoc.html",{"doctors":docs})

#User Login
def log(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        creds=Details.objects.filter(username=username,password=password)
        if creds:
            patid=creds[0].id
            response= render(request,"home.html",{
                "patient":patid
            })
            return response
        else:
            messages.error(request,"user does not exist")
            return HttpResponse("USER DOES NOT EXIST")
    else:
        return render(request,"login.html")

#User Home Page
def homepage(request):
    return render(request,"home.html")

#View Doctors
def doctors(request,pid):
    docs=Doctors.objects.all()
    if docs:
        return render(request,"doctors.html",{ "patient":pid, "doctors":docs})

#Book Appointments
def appointment(request,pid,did):
    if request.method=="POST":
        date=request.POST.get('date_time')
        desc=request.POST.get('desc')
        apps=Appointments.objects.filter(docid=did,appdate=date)
        if apps:
            return HttpResponse("APPOINTMENT UNAVAILABLE")
        else:
            patient=Details.objects.filter(id=pid)
            pname=patient[0].fname
            doctor=Doctors.objects.filter(docid=did)
            dname=doctor[0].docname
            query=Appointments(docid=did,docname=dname,pid=pid,pname=pname,appdate=date,desc=desc)
            query.save()
            appointments=Appointments.objects.filter(pid=pid)
            return render(request,"viewapps.html",{
                "patientapps":appointments,
            })
    else:
        doc=Doctors.objects.filter(docid=did)
        return render(request,"booking.html",{
            "patient":pid,
            "doctor":doc[0]
        })
    
#Book Appointments
def viewappointments(request,pid):
    appointments=Appointments.objects.filter(pid=pid)
    if appointments:
        return render(request,"viewapps.html",{
            "patientapps":appointments
        })
    else:
        return render(request,"viewapps.html")
    
def adminappointments(request):
   appointments=Appointments.objects.all()
   if appointments:
        return render(request,"viewapps.html",{
            "patientapps":appointments
        })
   else:
        return render(request,"viewapps.html")  
    
def admlog(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        creds=Adminlog.objects.filter(username=username,password=password)
        if creds:
            return render(request,"admin.html") 
        else:
            messages.error(request,"user does not exist")
            return HttpResponse("USER DOES NOT EXIST")
    else:
        return render(request,"admlog.html")
    
def dochome(request):
    if request.method=="POST":
        email=request.POST.get('username')
        password=request.POST.get('password')
        creds=Doctors.objects.filter(docemail=email,password=password)
        if creds:
            return render(request,"dochome.html")
        else:
            messages.error(request,"user does not exist")
            return HttpResponse("USER DOES NOT EXIST")

def addrecord(request):
    if request.method=='POST':
        pname=request.POST.get('pname') 
        dname=request.POST.get('dname')
        date=request.POST.get('date_time')
        age=request.POST.get('age')
        bldgrp=request.POST.get('bgrp')
        desc=request.POST.get('desc')
        nxtapp=request.POST.get('nextdt')
        tplan=request.POST.get('trtplan')
        patient=Details.objects.filter(fname=pname)
        pid=patient[0].id
        doctor=Doctors.objects.filter(docname=dname)
        did=doctor[0].docid
        query=Medrecord(docid=did,docname=dname,date=date,pid=pid,pname=pname,age=age,bldgrp=bldgrp,desc=desc,nxtapp=nxtapp,tplan=tplan)
        query.save()
        return HttpResponse("Saved Successfully")

def doclog(request):
    return render(request,"doclog.html")

def index(request):
    return render(request,"index.html")

def medrecord_list(request):
    records = Medrecord.objects.all()
    return render(request, 'admrecord.html', {'records': records})

def patmed(request,pid):
    records=Medrecord.objects.filter(pid=pid)
    return render(request,'admrecord.html',{'records':records})
