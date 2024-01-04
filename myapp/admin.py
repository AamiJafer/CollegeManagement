from django.contrib import admin
from myapp.models import Course,Student,userteacher

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(userteacher)
# Register your models here.
