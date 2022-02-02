from django.urls import path
from official.views import *
 
app_name = 'official'  

urlpatterns = [
    path('',addDistrict,name="addDistrict"),

    path('addBranch/',addBranch,name="addBranch"),
    path('log_in',log_in,name="log_in"),
    path('logout/', logout, name='logout'),
    path('addDoctor/',addDoctor,name="addDoctor"),
    path('addSchedule/',addSchedule,name="addSchedule"),
    
    path('delet/<str:id>',delet,name="delet"),
    path('deletbranch/<str:id>',deletbranch,name="deletbranch"),
    path('deletdoct/<str:id>',deletdoct,name="deletdoct"),
    path('deletsched/<str:id>',deletsched,name="deletsched"),
    
]