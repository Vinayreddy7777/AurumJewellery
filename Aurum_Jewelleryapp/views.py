from django.shortcuts import render, redirect
from Aurum_Jewelleryapp.models import ContactModel, UserRegistrationModel
import urllib.request
import urllib.parse
import random 
import ssl


#importing resources for messages.
from django.contrib import messages

def sendSMS(user, otp, mobile):
    data = urllib.parse.urlencode({
        'username': 'Codebook',
        'apikey': '56dbbdc9cea86b276f6c',
        'mobile': mobile,
        'message': f'Hello {user}, your OTP for account activation is {otp}. This message is Aurum Jewellery Website server. Thank you',
        'senderid': 'CODEBK'
    })
    data = data.encode('utf-8')
    # Disable SSL certificate verification
    context = ssl._create_unverified_context()
    request = urllib.request.Request("https://smslogin.co/v3/api.php?")
    f = urllib.request.urlopen(request, data,context=context)
    return f.read()


#MainPages Started Here.
def main_home(request):
    return render(request,'main-home.html')

def main_about(request):
    return render(request,'main-about.html')

def main_jewellery(request):
    return render(request,'main-jewellery.html')

#Admin Login Backend Start.
def main_admin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')         
               
        if email =='admin123@gmail.com' and password =='admin123@gmail.com':     
            messages.success(request,'Login Successful, but Dashboard is in Progress')
            return redirect('main_admin')
        else:        
            messages.error(request, "Invalid Login") 
    return render(request,'main-admin.html')
#Admin Login Backend end.

#ServiceProvider Login Backend Start.
def main_sp(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')         
               
        if email =='serviceprovider123@gmail.com' and password =='serviceprovider123@gmail.com':     
            messages.success(request,'Login Successful, but Dashboard is in Progress')
            return redirect('main_sp')
        else:        
            messages.error(request, "Invalid Login") 
    return render(request,'main-serviceproviders.html')
#ServiceProvider Login Backend end.

#User Registration Backend Start.
def main_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        password = request.POST.get('password')        
        if UserRegistrationModel.objects.filter(email=email).exists():
            messages.error (request, "Email already exist, try with other email.")                 
        else:
            user = UserRegistrationModel.objects.create(username=username, email=email, mobile=mobile, address=address, password=password)
            user.save()        
            messages.success(request, "Account created successful")
            return redirect('main_user')
        
    return render(request,'main-register.html')
#User Registration Backend End.

#User Login Backend Start.
def main_user(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        try:
            check=UserRegistrationModel.objects.get(email=email,password=password)
            request.session["user_id"]=check.user_id
            messages.success(request,'Login Successful')
            return redirect('user_home')
        except:
            messages.error(request, "Invalid Login") 
    return render(request,'main-user.html')
#User Login Backend End.


def main_fp(request):
    if request.method == "POST":
        number = request.POST.get('mobile')
        request.session['forgot_password_number'] = number
        otp = random.randint(1000,9999)
        request.session['otp_enterd_forgorpage']= otp
        user = "user"
        sendSMS(user,otp,number)
        print(number,otp)
        return redirect('main_otp')
    return render(request, 'main-forgotpassword.html')


def main_otp(request):
    if request.method == "POST":
        otp_from_prv_page = request.session.get('otp_enterd_forgorpage')
        print(otp_from_prv_page)
        otp_entered = request.POST.get('otp')
        print(otp_entered)
        if int(otp_entered) == int(otp_from_prv_page):
            print("otp matched !")
            return redirect('main_resetpassword')
        else:
            print("notmatched")
            messages.error(request,'OTP not matching, please try again')
            return redirect('main_otp')
    return render(request,'main-otp.html')


def main_resetpassword(request):
    if request.method == "POST":
        number = request.session.get('forgot_password_number')
        user = UserRegistrationModel.objects.get(mobile=number)
        new_password = request.POST.get('newpassword')
        user.password = new_password
        user.save()
        messages.success(request,"Reset Password Successful")
        return redirect('main_user')
    return render(request,'main-resetpassword.html')


def main_contact(request):
    if request.method == "POST":        
        username=request.POST.get('username')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        message=request.POST.get('message')      
      
        user=ContactModel.objects.create(username=username,email=email,mobile=mobile,message=message)
        user.save()
        
        if user:    
            messages.success(request, "Sent Successfully")
        else:
            messages.error(request, "Something Wrong, Please try again.")        
    return render(request,'main-contact.html')

def main_chatbot(request):
    return render(request,'main-chatbot.html')
#MainPages Ended Here.



#User Started Here.
def user_home(request):
    return render(request,'user-home.html')
#User Ended Here.