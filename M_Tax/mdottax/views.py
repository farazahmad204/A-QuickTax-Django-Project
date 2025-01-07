from django.shortcuts import redirect, render




import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



DEFAULT_FROM_EMAIL = 'farazahmed204@gmail.com'


# Create your views here.
def about_us(request):

    return render(request,'mdottax/pages/about_us.html')



def bookeeping_service(request):

    return render(request,'mdottax/pages/bookeeping_service.html')


def business_tax_service(request):

    return render(request,'mdottax/pages/business_tax_service.html')


def income_tax_service(request):

    return render(request,'mdottax/pages/income_tax_service.html')


def business_formation_and_ITIN(request):

    return render(request,'mdottax/pages/business_formation_and_ITIN.html')



def home(request):

    return render(request,'mdottax/pages/home.html')


def error(request):

    return render(request,'mdottax/pages/error.html')

def salestax(request):

    return render(request,'mdottax/pages/salestax.html')
    