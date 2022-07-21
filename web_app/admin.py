from django.contrib import admin

# Register your models here.
from .models import*

admin.site.register(Students)
admin.site.register(QRCodes)
admin.site.register(Courses)
admin.site.register(Enrollments)
admin.site.register(Actions)
admin.site.register(Achievements)
admin.site.register(Achieved)
