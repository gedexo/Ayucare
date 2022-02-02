from django.contrib import admin
from .models import Branch,Doctor,Schedule,DistrictMap
# Register your models here.

admin.site.register(Branch)
admin.site.register(Doctor)
admin.site.register(DistrictMap)





@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('branch','doctor','start_time','end_time')