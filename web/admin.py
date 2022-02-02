from django.contrib import admin
from .models import Subscribe, Treatment,Gallery,Contact,Testimonial


@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display =('title','summary')


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass

@admin.register(Subscribe) 
class SubscribeAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    pass
