from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index,name="index"),
    path('about/',views.about,name="about"),
    path('branch/',views.branch,name="branch"),
    path('contact/',views.contact,name="contact"),
    path('doctors/',views.doctors,name="doctors"),
    path('galleries/',views.galleries,name="gallery"),
    path('products/',views.products,name="products"), 
    path('book/<int:id>',views.book,name="book"), 

    path('branchmark/',views.branchmark,name="branchmark"),
    path('districtsr/',views.districtsr,name="districtsr"),

    path('branchbook/<int:id>/',views.branchbook,name="branchbook"),
    path('email/',views.email,name="email"),

]