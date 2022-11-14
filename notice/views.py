from audioop import reverse
from contextlib import redirect_stderr
import email
import imp
from importlib import import_module
from inspect import modulesbyfile
from re import template
from unittest import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from .models import noticeboard, teacher, galleries, testimonial
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.template import loader
# Create your views here.

def notice(request):
    note = noticeboard.objects.all().order_by('-id')

    return render(request, 'notice.html', {'notes': note})


def index(request):
    profil = teacher.objects.all().order_by('position')
    notes = noticeboard.objects.all().order_by('-id')
    return render(request, 'index.html', {'notes': notes,'profile': profil})


def teachers(request):
    profil = teacher.objects.all().order_by('position')
    return render(request, 'teachers.html', {'profile': profil})


def gallery(request):
    imges = galleries.objects.all().order_by('-id')
    return render(request, 'gallery.html', {'img': imges})


def testimonials(request):
    profile = testimonial.objects.all().order_by('-id')
    return render(request, 'testimonials.html', {'profile': profile})

def about(request):
    return render(request, 'about.html')


def ad_process(request):
    return render(request, 'ad_process.html')

def maintenance(request):
    return render(request, 'maintenance.html')

def admission(request):
        return render(request, 'admission.html')

def contact(request):
    return render(request, 'contact.html')

def contacts(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    comments = request.POST.get('comments')

    template= loader.get_template('contact.txt')
    data ={
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone':phone,
        'comments':comments
    }
    message = template.render(data)
    subject = "You've been contacted by {} {}".format(data['first_name'],data['last_name'])
    email = EmailMessage(subject , message, '', ['hbssint@gmail.com'])
    email.content_subtype ='html'
    email.send()

        
    return render(request, 'contacts.html',{'name': first_name})



def logout(request):
    auth.logout(request)
    return redirect('/')

def admissions(request):
    session = request.POST.get('session')
    std = request.POST.get('std')
    date= request.POST.get('date')
    aadhar= request.POST.get('aadhar')
    gender= request.POST.get('gender')
    dob= request.POST.get('dob')
    category= request.POST.get('category')
    caste= request.POST.get('caste')
    religion= request.POST.get('religion')
    nationality= request.POST.get('nationality')
    pre_school= request.POST.get('pre_school')
    pre_class= request.POST.get('pre_class')
    pre_year= request.POST.get('pre_year')
    percentage= request.POST.get('percentage')
    add_1= request.POST.get('add_1')
    add_2= request.POST.get('add_2')
    city= request.POST.get('city')
    state= request.POST.get('state')
    pincode= request.POST.get('pincode')
    f_name= request.POST.get('f_name')
    f_occu= request.POST.get('f_occu')
    m_name= request.POST.get('m_name')
    m_occu= request.POST.get('m_occu')
    f_aadhar= request.POST.get('f_aadhar')
    f_qual= request.POST.get('f_qual')
    m_qual= request.POST.get('m_qual')
    income= request.POST.get('income')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')

    template= loader.get_template('admission.txt')
    data ={
        'first_name': first_name,
        'last_name': last_name,
        'email' : email,
        'phone' : phone,
        'session' : session,
        'std' : std,
        'date' : date,
        'aadhar' : aadhar,
        'gender' : gender,
        'dob' : dob,
        'category' : category,
        'caste' : caste,
        'religion' : religion,
        'nationality' : nationality,
        'pre_school' : pre_school,
        'pre_class' : pre_class,
        'pre_year' : pre_year,
        'percentage' : percentage,
        'add_1' : add_1,
        'add_2' : add_2,
        'city' : city,
        'state' : state,
        'pincode' : pincode,
        'f_name' : f_name, 
        'f_occu' : f_occu,
        'm_name' : m_name,
        'm_occu' : m_occu,
        'f_aadhar' : f_aadhar,
        'f_qual' : f_qual,
        'm_qual' : m_qual,
        'income' : income

    }
    message = template.render(data)
    subject = "The Admission form has been submitted by {} {}".format(data['first_name'],data['last_name'])
    
    email = EmailMessage(subject , message, '', ['hbssint@gmail.com'])
    email.content_subtype = 'html'

    
    file1 = request.FILES['t_cer']
    file2 = request.FILES['p_receipt']
    email.attach(file1.name, file1.read(), file1.content_type)
    email.attach(file2.name, file2.read(), file2.content_type)
    email.send()

    subject2 = "The Admission form submitted successfully..!!"
    email2 = EmailMessage(subject2, message, '', [data['email']])
    email2.content_subtype = 'html'

    email2.attach(file1.name, file1.read(), file1.content_type)
    email2.attach(file2.name, file2.read(), file2.content_type)
    email2.send()

        
    return render(request, 'admissions.html',{'name': first_name})