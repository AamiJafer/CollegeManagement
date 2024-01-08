from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login
from myapp.models import Course,Student,userteacher
import os

def loginpage(request):
    return render(request,'login.html')

def adminhome(request):
    if request.user.is_authenticated and request.user.is_staff:
        return render(request,'adminhome.html')
    return redirect('loginpage')


def userhome(request):
    if request.user.is_authenticated:
        return render(request,'userhome.html')
    return redirect('loginpage')

def coursepage(request):
    if request.user.is_authenticated:
        return render(request,'course.html')
    else:
        messages.info(request,'Please Login!!')
        return redirect('loginpage')

def checklogin(request):
    if request.method=='POST':
        u_name=request.POST['usename']
        passwrd=request.POST['pass']
        user=auth.authenticate(username=u_name,password=passwrd)
        if user is not None:
            if user.is_staff:
                login(request,user)
                messages.info(request,f'Login Successful {u_name}')
                return redirect('adminhome')
            else:
                login(request,user)
                messages.info(request,f'Login Successful {u_name}')
                return redirect('userhome')
        else:
            messages.info(request,'Please enter valid Username and Password')
            return redirect('loginpage')
    else:
        return redirect('loginpage')

def saveCourse(request):
    if request.method=="POST":
        name=request.POST['c_name']
        fee=request.POST['c_fee']
        course=Course(course_name=name,course_fee=fee)
        course.save()
        return redirect('addStudent')

def addStudent(request):
    if request.user.is_authenticated:
        course=Course.objects.all()
        return render(request,'student.html',{'course':course})

def saveStudent(request):
    if request.method=="POST":
        name=request.POST['s_name']
        addr=request.POST['s_add']
        age=request.POST['s_age']
        date=request.POST['jod']
        cid=request.POST['course']
        course=Course.objects.get(id=cid)
        student=Student(course=course,student_name=name,student_address=addr,student_age=age,joining_date=date)
        student.save()
        return redirect('displayStudent')
    
def displayStudent(request):
    if request.user.is_authenticated:
        stud=Student.objects.all()
        return render(request,'displayStud.html',{'stud':stud})

def editStudent(request,pk):
    course=Course.objects.all()
    stud=Student.objects.get(id=pk)
    return render(request,'editStudent.html',{'stud':stud,'course':course})

def updateStudent(request,pk):
    if request.method=="POST":
        student=Student.objects.get(id=pk)
        student.student_name=request.POST['s_name']
        student.student_address=request.POST['s_add']
        student.student_age=request.POST['s_age']
        student.joining_date=request.POST['jod']
        courseid=request.POST['course']
        student.course=Course.objects.get(id=courseid)
        student.save()
        return redirect('displayStudent')
    
def deleteStudent(request,pk):
    stud=Student.objects.get(id=pk)
    stud.delete()
    return redirect('displayStudent')

def addTeacher(request):
        course=Course.objects.all()
        return render(request,'addTeacher.html',{'course':course})

def saveTeacher(request):
    if request.method=='POST':
        f_name=request.POST.get('fname')
        l_name=request.POST.get('lname')
        u_name=request.POST.get('uname')
        passwrd=request.POST.get('password')
        cpasswrd=request.POST.get('cpassword')
        addr=request.POST.get('address')
        age=request.POST.get('age')
        email=request.POST.get('email')
        number=request.POST.get('mob')
        image=request.FILES.get('img')
        cid=request.POST['course']
        course=Course.objects.get(id=cid)
        if passwrd==cpasswrd:
            if User.objects.filter(username=u_name).exists():
                messages.info(request,'This username already exists!!')
                return redirect('addTeacher')
            else:
                user=User.objects.create_user(first_name=f_name,last_name=l_name,username=u_name,password=passwrd,email=email)
                user.save()
                teacher=userteacher(course=course,user=user,address=addr,age=age,mobile=number,image=image)
                teacher.save()
                return redirect('addTeacher')
        else:
            messages.info(request,'Password Doesnt match!!')
            return redirect('addTeacher')
    else:
        return redirect('addTeacher')
    
def editTeacher(request):
    if request.user.is_authenticated:
        course=Course.objects.all()
        current_userid=request.user.id
        teacher=userteacher.objects.get(user_id=current_userid)
        return render(request,'editTeacher.html',{'teacher':teacher,'course':course})

def teacherCard(request):
    if request.user.is_authenticated:
        current_userid=request.user.id
        teacher=userteacher.objects.get(user_id=current_userid)
        return render(request,'teacherCard.html',{'teacher':teacher})
    
def updateTeacher(request):
    if request.user.is_authenticated:
        pk=request.user.id
        if request.method=='POST':
            details1=userteacher.objects.get(user_id=pk)
            details2=User.objects.get(id=pk)
            if len(request.FILES)!=0:
                if len(details1.image)>0:
                    os.remove(details1.image.path)
                details1.image=request.FILES.get('img')
            details2.first_name=request.POST.get('fname')
            details2.last_name=request.POST.get('lname')
            details2.username=request.POST.get('uname')
            # password=request.POST.get('password')
            # if password:
            #     details2.password = make_password(password)
            details1.address=request.POST.get('address')
            details1.age=request.POST.get('age')
            details2.email=request.POST.get('email')
            details1.mobile=request.POST.get('mob')
            cid=request.POST['course']
            details1.course=Course.objects.get(id=cid)
            details1.save()
            details2.save()
            return render(request,'teacherCard.html',{'teacher':details1})
        return redirect('editTeacher') 
    return redirect('editTeacher') 
     
    
def showTeacher(request):
    if request.user.is_authenticated:
        teacher=userteacher.objects.all()
        return render(request,'showTeacher.html',{'teacher':teacher})
    
def deleteTeacher(request,pk):
        teacher=userteacher.objects.get(id=pk)
        if teacher.image:
            teacher.image.delete()
        teacher.delete()
        teacher.user.delete()
        return redirect('showTeacher')

def logoutuser(request):
    if request.user.is_authenticated:
        messages.info(request,'Logout Successfull')
        auth.logout(request)
    return redirect('/')











        





# Create your views here.