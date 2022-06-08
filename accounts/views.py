from base64 import urlsafe_b64encode
from email.message import EmailMessage
from multiprocessing import context
from django.shortcuts import redirect, render

from accounts.models import Account
from .forms import Registrationform
from .models import Account
from django.contrib import messages ,auth
from django.contrib.auth.decorators import login_required

# verification Email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage




# Create your views here.

def register(request):
    if request.method == 'POST':
        form = Registrationform(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
            user.phone_number = phone_number
            user.save()


            # USER ACTIVATION
            # current_site = get_current_site(request)
            # mail_subject = 'Please activate your Account'
            # message      = render_to_string('accounts/account_verification_email.html',{
            #     'user' : user,
            #     'domain' : current_site,
            #     'uid'    : urlsafe_b64encode(force_bytes(user.pk)),
            #     'token'  : default_token_generator.make_token(user),


            # })
            # to_email = email
            # send_email = EmailMessage(mail_subject,message,to=[to_email])
            # send_email.send()
            messages.success(request,"Registration Successfull")
            return redirect('register')
    else:
        form = Registrationform()
    context = {
        'form':form,
    }

    return render(request,'accounts/register.html',context)


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email , password = password)

        if user is not None:
            auth.login(request, user)
            messages.success(request,'Your are Now Logged In')
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid login Credentials")
            return redirect('login')
                

    return render(request,'accounts/login.html')


@login_required(login_url= '/login')
def logout(request):
    auth.logout(request)
    messages.success(request,"Your Loggout Out Successfully.")
    return redirect('login')  



@login_required(login_url= '/login')
def dashboard(request):
    return render(request,'accounts/dashboard.html')



def forgotpassword(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        reenterpassword=request.POST['reenterpassword']

        if password ==reenterpassword:
            user.set_password(password)
            user.save()
            messages.success(request,"Password set successfull")
            return redirect('login')

        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__iexact=email)

            messages.success(request,"Password set Sucessfull")
            return redirect('login')
    else:
        messages.error(request,"Account Does Not Exists")
        # return redirect('login')
    return render(request,'accounts/forgotpassword.html')






