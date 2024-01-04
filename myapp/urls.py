from django.urls import path
from . import views

urlpatterns = [
    path('',views.loginpage,name="loginpage"),
    path('adminhome',views.adminhome,name="adminhome"),
    path('userhome',views.userhome,name="userhome"),
    path('checklogin',views.checklogin,name="checklogin"),
    path('coursepage',views.coursepage,name="coursepage"),
    path('saveCourse',views.saveCourse,name="saveCourse"),
    path('addStudent',views.addStudent,name="addStudent"),
    path('saveStudent',views.saveStudent,name="saveStudent"),
    path('displayStudent',views.displayStudent,name="displayStudent"),
    path('editStudent/<int:pk>',views.editStudent,name="editStudent"),
    path('updateStudent/<int:pk>',views.updateStudent,name="updateStudent"),
    path('deleteStudent/<int:pk>',views.deleteStudent,name="deleteStudent"),
    path('addTeacher',views.addTeacher,name="addTeacher"),
    path('saveTeacher',views.saveTeacher,name="saveTeacher"),
    path('editTeacher',views.editTeacher,name="editTeacher"),
    path('updateTeacher',views.updateTeacher,name="updateTeacher"),
    path('teacherCard',views.teacherCard,name="teacherCard"),
    path('showTeacher',views.showTeacher,name="showTeacher"),
    path('deleteTeacher/<int:pk>',views.deleteTeacher,name="deleteTeacher"),
    path('logoutuser',views.logoutuser,name="logoutuser")
]
