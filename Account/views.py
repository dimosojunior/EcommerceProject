from django.db.models.query import QuerySet
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, FormView, DetailView, DeleteView, UpdateView, ListView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.db.models import Q
import datetime
from django.core.mail import send_mail
from django.conf import settings

from MyApp.models import *
from MyApp.forms import *

from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth


# Create your views here.
def signup(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        #role = request.POST['role']

        if password == password2:
            if MyUser.objects.filter(email=email).exists():
                messages.info(request, f"Email {email} Already Taken")
                return redirect('signup')
            elif MyUser.objects.filter(username=username).exists():
                messages.info(request, f"Username {username} Already Taken")
                return redirect('signup')
            else:
                user = MyUser.objects.create_user(username=username, email=email, password=password)
                user.save()


                #HIZI NI KWA AJILI KUTUMA EMAIL ENDAPO MTU AKIJISAJILI
                username = request.POST.get('email')
                #last_name = request.POST['last_name']
                email = request.POST.get('email')
                subject = "Welcome to DIMOSO ELECTRONICS CENTER"
                message = f"Ahsante  {username} kwa kujisajili kwenye mfumo wetu kama {username} email yako {email}. Nunua bidhaa bora na kwa bei nafuu kupitia Dimoso Electronics Center, unaweza kuweka order au kunitumia email kwa ajili ya kupata bidhaa zako kwa haraka. Ahsante {username} endelea kutembelea mfumo wetu "
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail(subject, message, from_email, recipient_list, fail_silently=True)



                # #log user in and redirect to settings page
                user_login = auth.authenticate(email=email, password=password)
                auth.login(request, user_login)

                
                return redirect('home')
        else:
            messages.info(request, 'The Two Passwords Not Matching')
            return redirect('signup')

    else:
        return render(request, 'Account/signup.html')

def signin(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')

    else:
        return render(request, 'Account/signin.html')



def signin2(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')

    else:
        return render(request, 'Account/signin2.html')

@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')







#---------------------THIS IS FOR MY ACCOUNT----------------------------->

def signup_for_my_account(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        #role = request.POST['role']

        if password == password2:
            if MyUser.objects.filter(email=email).exists():
                messages.info(request, f"Email {email} Already Taken")
                return redirect('my_account')
            elif MyUser.objects.filter(username=username).exists():
                messages.info(request, f"Username {username} Already Taken")
                return redirect('my_account')
            else:
                user = MyUser.objects.create_user(username=username, email=email, password=password)
                user.save()


                #HIZI NI KWA AJILI KUTUMA EMAIL ENDAPO MTU AKIJISAJILI
                username = request.POST.get('email')
                #last_name = request.POST['last_name']
                email = request.POST.get('email')
                subject = "Welcome to DIMOSO ELECTRONICS CENTER"
                message = f"Ahsante  {username} kwa kujisajili kwenye mfumo wetu kama {username} email yako {email}. Nunua bidhaa bora na kwa bei nafuu kupitia Dimoso Electronics Center, unaweza kuweka order au kunitumia email kwa ajili ya kupata bidhaa zako kwa haraka. Ahsante {username} endelea kutembelea mfumo wetu "
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail(subject, message, from_email, recipient_list, fail_silently=True)



                # #log user in and redirect to settings page
                user_login = auth.authenticate(email=email, password=password)
                auth.login(request, user_login)

                
                return redirect('home')
        else:
            messages.info(request, 'The Two Passwords Not Matching')
            return redirect('my_account')

    

def signin_for_my_account(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('my_account')





