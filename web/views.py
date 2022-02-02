from django.db import models
from django.http.response import Http404, JsonResponse
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
from web.models import Gallery, Treatment ,Subscribe,Testimonial
from official.models import Branch, Doctor,Schedule,DistrictMap
from .forms import ContactForm,SubscribeForm


def index(request):
    treatment = Treatment.objects.all()
    testimonial = Testimonial.objects.filter().order_by('-id')[:4]
    doctors=Doctor.objects.filter(inHomeScreen=True)
    context = {
        "is_index" : True,
        "treatment":treatment,
        "testimonial":testimonial,
        "doctors":doctors,
    }
    return render(request, 'web/index.html',context)

  
def about(request):
    context = {
        "is_about" : True
    }
    return render(request, 'web/aboutus.html',context)


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            response_data = {
                "status" : "true",
                "title" : "Sent Successfully",
                "message" : "Message successfully updated"
            }
        else:
            print (form.errors)
            response_data = {
                "status" : "false",
                "title" : "Form validation error",
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
            'is_contact' : True,
            'form' : form,
        }
    return render(request, 'web/contact.html',context)


def galleries(request):
    galleries = Gallery.objects.all()
    context = {
        "is_gallery" : True,
        "galleries" : galleries,
    }
    return render(request,'web/gallery.html',context)


def products(request):
    context = {
        "is_products" : True
    }
    return render(request, 'web/products.html',context)



def doctors(request):
    doctors = Doctor.objects.all()
    class DoctorandSchedule:
        def __init__(self,doctor,schedules,count):
            self.doctor = doctor
            self.schedules = schedules
            self.count = count

    DoctorandSchedules=[]

    for d in doctors:
        DoctorandSchedules.append(DoctorandSchedule(d,d.schedule_set.all(),d.schedule_set.filter().exists))
    
    
    context = {
        "is_doctors" : True,
        
        "DoctorandSchedules":DoctorandSchedules,
    }
    return render(request, 'web/doctor.html',context)


def branch(request):
    districtmap = DistrictMap.objects.all()
    
    context = {
        "is_branch" : True,
        "districtmap":districtmap,
    }
    
    return render(request, 'web/branch.html',context)


def branchbook(request,id):
    branch = get_object_or_404(Branch,id=id)
    schedules = Schedule.objects.filter(branch = branch)
    whatsappbtn = ''
    brname = ''
    brnumber = ''
    brday = ''
    if request.POST:
        scheduleID = request.POST['scheduleID']
        brname = request.POST['brname']
        brnumber = request.POST['brnumber']
        brday = request.POST['brday']
        
        scheduleselect = Schedule.objects.get(id=scheduleID)

        start = scheduleselect.start_time.strftime("%I:%M %p")
        end = scheduleselect.end_time.strftime("%I:%M %p")

        whatsappbtn = 'https://wa.me/+91'+str(branch.phone)

        messagestring = '?text=Patient Name : '+brname+'%0aPatient Number : '+brnumber+'%0aDay : '+brday+\
                "%0a*-----Booking Details------*"

        messagestring += '%0aBranch : '+branch.name+\
                         '%0aLocation : '+branch.location+\
                         '%0aDoctor : '+scheduleselect.doctor.name+\
                         '%0aTime : '+str(start)+' - '+str(end)

        whatsappbtn += messagestring

        schedules = Schedule.objects.filter(id=scheduleID)
    context = {
        "is_branchbook" : True,
        "branch":branch,
        "schedules":schedules,   
        "whatsappbtn":whatsappbtn,
        "brname":brname,
        "brnumber":brnumber,
        "brday":brday,
    }
    return render(request, 'web/branchbook.html',context)


def book(request,id):
    schedule = get_object_or_404(Schedule,id=id)
    if request.POST:
        ptname = request.POST['ptname']
        ptnumber = request.POST['ptnumber']
        ptday = request.POST['ptday']
        start = schedule.start_time.strftime("%I:%M %p")
        end = schedule.end_time.strftime("%I:%M %p")
        whatsappbtn = 'https://wa.me/+91'+str(schedule.branch.phone)
        messagestring = '?text=Patient Name : '+ptname+'%0aPatient Number : '+ptnumber+'%0aBooking Day : '+ptday+\
                "%0a*-----Booking Details------*"
        messagestring += '%0aBranch : '+schedule.branch.name+\
                         '%0aLocation :'+schedule.branch.location+\
                         '%0aDoctor : '+schedule.doctor.name+\
                         '%0aTime : '+str(start)+' - '+str(end)
        whatsappbtn += messagestring
        context = {
        "is_book" : True,
        "schedule":schedule,
        "whatsappbtn":whatsappbtn,
        "ptname":ptname,
        "ptnumber":ptnumber,
        "ptday":ptday
        }
        
        return render(request, 'web/book.html',context)
    context = {
        "is_book" : True,
        "schedule":schedule,
    }
    return render(request, 'web/book.html',context)


def branchmark(request):
    branchmark = list(Branch.objects.values())
    return JsonResponse(branchmark, safe=False)


def districtsr(request):
    districtsr = list(DistrictMap.objects.values())
    return JsonResponse(districtsr, safe=False)


def email(request):
    email_form = SubscribeForm(request.POST or None)
    if request.method == 'POST':
        if email_form.is_valid():
            email_form.save()
            response_data = {
                "status" : "true",
                "title" : "Subscribe Successfully",
                "message" : "Get in Touch With U Soon !"
            }
        else:
            print (email_form.errors)
            response_data = {
                "status" : "false",
                "title" : "Form validation error",
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        return Http404("Poll Does not Exist")
  

