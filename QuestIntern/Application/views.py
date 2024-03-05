from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from .models import Job
import random

def startup(request):
    jobs = Job.objects.all()
    return render(request, 'home.html', {'jobs': jobs})

def usignup(request):
    return render(request,'signup.html')

def signingup(request):
    if request.method =='POST':
        uname = request.POST['user-name']
        upass = request.POST['user-password']
        umail = request.POST['user-email']
        if umail.__contains__('@srmist.edu.in'):
            # Mail
            subject = 'Greetings from Quest Intern'
            otp = random.randint(1000,9999)
            message = 'Welcome '+ uname+' for Logging in QuestIntern \n Your Otp is '+str(otp)
            from_email = settings.EMAIL_HOST_USER 
            to_list = [umail]
            try:
                send_mail(subject,message,from_email,to_list,fail_silently=True)
            except Exception as e :
                print(e)
            myuser = User.objects.create_user(uname,umail,upass)
            myuser.save()
            alert_message='Congragulations!! '+uname+', Your InternQuest Account has been Successfully Created.'
            messages.success(request,alert_message)
            response = redirect('/')
            return response
        else:
            alert_message='Sorry '+uname+', Please login with your SRM email'
            messages.warning(request,alert_message)
            response = redirect('/')
            return response

def ulogin(request):
    if request.method == "POST":
        uname = request.POST['user-name']
        upass = request.POST['user-password']
        user = authenticate(username=uname,password=upass)
        if user is not None:
            login(request,user)
             # Welcome Mail
            subject = 'Greetings from InternQuest'
            msg= 'Hi '+uname+' you are now logged in'
            message = 'Hi '+uname +' A Login Activity Detected For your Account... '
            from_email = settings.EMAIL_HOST_USER 
            to_list = [user.email]  
            send_mail(subject,message,from_email,to_list,fail_silently=True)
            messages.success(request,msg)
            return redirect('/')
        else:
            return HttpResponse('Wrong Password')
    else:
        return HttpResponse("Post Error ")    

def ulogout(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")
    else:
        return HttpResponse('No access')

def add_job(request):
    return render(request,'add_jobs.html')

def insert_job(request):
    if request.method == 'POST':
        url = request.POST['job_url']
        company = request.POST['company']
        salary = request.POST['salary']
        year_from = request.POST['year_from']

        posted_by = request.user.username
        job = Job.objects.create(
            url=url,
            posted_by=posted_by,
            company=company,
            salary=salary,
            year_from=year_from
        )
        return redirect('/')
    else:
        return render(request, 'home.html')
    