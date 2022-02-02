from django.db import models
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
from official.forms import BranchForm,DoctorForm,ScheduleForm,DistrictMapForm,GalleryForm
from .models import Branch, DistrictMap, Doctor, Schedule 
from web.models import Gallery
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib import messages 
from django.contrib import auth




def log_in(request):
    if request.user.is_authenticated:
        return redirect ('official:addDistrict')
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username is not None and password is not None:
            user=authenticate(username=username, password=password)     
            if user is not None:
                login(request, user)
                return redirect("/official/")
            else:   
                messages.error(request, "Invalid Details") 
        else:
            messages.error(request,None)

    return render (request, 'official/login.html')  


def logout(request):
    auth.logout(request)
    return redirect('official:log_in')


@login_required(login_url='official:log_in')
def addDistrict(request):
    districtlist = DistrictMap.objects.all()
    districtform = DistrictMapForm(request.POST or None)

    if request.method == 'POST':
        if request.POST.get('id') != '0':
            editDistrictMap = DistrictMap.objects.get(id =request.POST.get('id'))
            editDistrictMap.name = request.POST.get('name')
            editDistrictMap.latitude = request.POST.get('latitude')
            editDistrictMap.longitude = request.POST.get('longitude')
            editDistrictMap.save()
            response_data = {
                        "status" : "true",                 
                        "message" : "District Edited"
                    }
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')

        else: 
            if districtform.is_valid():
                districtform.save()          
                response_data = {
                        "status" : "true",
                        "title" : "Successfully Added",
                        "message" : "District Added"
                    }
            else:
                response_data = {
                    "status" : "false",
                    "title" : "Form validation error",
                }
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
                "is_addDistrict" : True,
                "districtform":districtform,
                "districtlist":districtlist,
        }
    return render(request, 'official/addDistrict.html',context)


@login_required(login_url='official:log_in')
def addBranch(request):
    branchlist = Branch.objects.all()
    branchform = BranchForm(request.POST or None)

    if request.method == 'POST':
        if request.POST.get('id') != '0':
            editBranch = Branch.objects.get(id =request.POST.get('id'))
            editBranch.name = request.POST.get('name')
            editBranch.title = request.POST.get('title')
            editBranch.phone = request.POST.get('phone')
            editBranch.location = request.POST.get('location')
            editBranch.latitude = request.POST.get('latitude')
            editBranch.longitude = request.POST.get('longitude')
            editBranch.save()
            response_data = {
                        "status" : "true",
                        "message" : "Branch Edited"
                    }
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
        else:
            if branchform.is_valid():
                branchform.save()          
                response_data = {
                        "status" : "true",
                        "title" : "Successfully Added",
                        "message" : "Branch Added"
                    }
            else:
                response_data = {
                    "status" : "false",
                    "title" : "Form validation error",
                }
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
            "is_addBranch" : True,
            "branchform":branchform,
            "branchlist":branchlist,
        }

    return render(request, 'official/addBranch.html',context)


@login_required(login_url='official:log_in')
def addDoctor(request):
    doctorlist = Doctor.objects.all()
    doctorform = DoctorForm(request.POST,request.FILES)

    if request.method == 'POST':
        if request.POST.get('id') != '0':
            editDoctor = Doctor.objects.get(id =request.POST.get('id'))
            editDoctor.register_number = request.POST.get('register_number')
            editDoctor.name = request.POST.get('name')
            if request.FILES.get('image'):
                editDoctor.image = request.FILES.get('image')
            editDoctor.qualification = request.POST.get('qualification')
            editDoctor.save()
            response_data = {
                        "status" : "true",                 
                        "message" : "Doctor Edited"
                    }
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
        else:

            if doctorform.is_valid():
                doctorform.save()          
                response_data = {
                    "status" : "true",
                    "title" : "Successfully Added",
                    "message" : "Doctor Added"
                }
            else:
                response_data = {
                    "status" : "false",
                }
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
            "is_addDoctor" : True,
            "doctorform":doctorform,
            "doctorlist":doctorlist,
        }
    return render(request, 'official/addDoctor.html',context)



@login_required(login_url='official:log_in')
def addGallery(request):
    galleryItems = Gallery.objects.all()
    galleryForm = GalleryForm(request.POST,request.FILES)

    if request.method == 'POST':
        if galleryForm.is_valid():
            galleryForm.save()          
            response_data = {
                "status" : "true",
                "title" : "Successfully Added",
                "message" : "Doctor Added"
            }
        else:
            response_data = {
                "status" : "false",
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
            "is_addDoctor" : True,
            "galleryForm":galleryForm,
            "galleryItems":galleryItems,
        }
    return render(request, 'official/gallery.html',context)


@login_required(login_url='official:log_in')
def addSchedule(request):
    schedulelist = Schedule.objects.all()
    scheduleform = ScheduleForm(request.POST or None)

    if request.method == 'POST':
        if request.POST.get('id') != '0':
            editSchedule = Schedule.objects.get(id =request.POST.get('id'))
            editSchedule.treatment = request.POST.get('treatment')
            editSchedule.branch.id = int(request.POST.get('branch'))
            editSchedule.doctor.id = int(request.POST.get('doctor'))
            editSchedule.day = request.POST.get('day')
            editSchedule.start_time = request.POST.get('start_time')
            editSchedule.end_time = request.POST.get('end_time')
            editSchedule.save()
            response_data = {
                        "status" : "true",
                        "message" : "Schedule Edited"
                    }
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
        else:
            if scheduleform.is_valid():
                scheduleform.save()          
                response_data = {
                        "status" : "true",
                        "title" : "Successfully Added",
                        "message" : "Schedule Added"
                    }
            else:
                response_data = {
                    "status" : "false",
                    "title" : "Form validation error",
                }
            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
            "is_addSchedule" : True,
            "scheduleform":scheduleform,
            "schedulelist":schedulelist,
        }
    
    return render(request, 'official/addSchedule.html',context)


def delet(request,id):
    object = DistrictMap.objects.get(id=id)
    object.delete()
    return redirect("/official/") 

def deletbranch(request,id):
    object = Branch.objects.get(id=id)
    object.delete()
    return redirect("/official/addBranch")

def deletdoct(request,id):
    object = Doctor.objects.get(id=id)
    object.delete()
    return redirect("/official/addDoctor")


def deletsched(request,id):
    object = Schedule.objects.get(id=id)
    object.delete()
    return redirect("/official/addDoctor")

