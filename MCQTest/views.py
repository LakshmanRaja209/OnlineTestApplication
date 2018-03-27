import string
import random
from django.shortcuts import render
from django.core.paginator import PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from MCQTest.models import *
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.http import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.contrib.auth.models import User
from MCQTest.forms import *
from django.conf import settings
from OnlineTest.settings import *
from django.db.models import Q
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib import messages
from django.core.exceptions import *
from django.core.urlresolvers import reverse
from django.template.loader import get_template
from django.template import Context
from django.template.loader import render_to_string
from datetime import date
# Create your views here.

def register_view(request):
    if request.method == 'POST':
        fn = request.POST.get('firstname')
        ln = request.POST.get('lastname')
        em = request.POST.get('email')
        un = request.POST.get('username')
        ps = request.POST.get('password')
        gn = request.POST.get('gender')
        mb = request.POST.get('phno')
        ad = request.POST.get('add')
        cn = request.POST.get('country')
        st = request.POST.get('state')
        ct = request.POST.get('city')
        pin = request.POST.get('pin_code')
        user = User(username = un, first_name = fn, last_name = ln, password = ps, email = em)
        user.save()
        user = User.objects.get(username=un)
        user.set_password(ps)
        user.save()
        pro = UserProfile(gender=gn, phone_number=mb, address = ad, country = cn, state = st, city = ct, pin_code = pin, user=user)
        pro.save()
        text = 'Thank You for registering to our Web site. http://' + request.get_host() + '/login/ Click Here to Login to MCQ Test Website. Hope you will enjoy our service.'
        email = EmailMessage('Registration', text, 'lakshmanraja209@gmail.com', [em])
        email.send()
        return HttpResponseRedirect('/login/')
    return render(request, 'MCQTest/registration.html')

def reset_view(request):
    return render(request,'MCQTest/reset.html')

@login_required(login_url='/login/')
def dashboard_view(request, pid = None):
    if pid is None:
        c = Category.objects.all()
        exist = TestSchedule.objects.filter(user = request.user).filter(attended = False).exists()
        activetest = [];
        notactive = [];
        if exist:
            activetest = TestSchedule.objects.filter(user = request.user).filter(attended = False)
        exist = TestSchedule.objects.filter(user = request.user).filter(attended = True).exists()
        if exist:
            notactive = TestSchedule.objects.filter(user = request.user).filter(attended = True)
        return render(request,'MCQTest/dashboard.html', {'cat' : c, 'activetest':activetest,'notactive':notactive})
    else:
        return HttpResponseRedirect('/home/'+ str(pid))

@login_required(login_url='/login/')
def practice_view(request, pid= None):
    msg = ''
    if request.method == 'POST':
        questions = request.POST.get('Que');
        list = [];
        result = [];
        total = 0;
        correct_answers = 0;
        wrong_ansers = 0;
        for i in questions:
            if i.isdigit():
                list.append(i);
                total = total + 1;
        c = 0;
        correction = '';
        for item in list:
            answered = Answers.objects.get(id = item);
            choice = request.POST.get(item);
            if choice is not None:
                c = c + 1;
                if str(answered.answer.id) == str(choice):
                    correction = " Question " + item + ": <b>Correct</b>";
                    correct_answers = correct_answers + 1;
                else:
                    correction = " Question " + item + ": Worng"; + 1;
                    wrong_ansers = wrong_ansers + 1;
                result.append(correction);
        correction = " Total No. Questions : " + str(total)
        result.append(correction);
        correction = " Total No. Questions attened : " + str(c);
        result.append(correction);
        correction = " Total No. Correct Answers : " + str(correct_answers)
        result.append(correction);
        correction = " Total No. Wrong Answers : " + str(wrong_ansers);
        result.append(correction);
        per = correct_answers/total*100;
        correction = " Percentage % : " + str(round(per));
        result.append(correction);
        if per > 60:
            msg = '<b>Thanks for your successful attempt Good Luck.</b>  We will send you the result sheet to your registered Mail ID.';
        else:
            if per > 45:
                msg = '<b>Thanks for your good attempt Good Work you are near to your target.</b>  We will send you the result sheet to your registered Mail ID.';
            else:
                msg = '<b>Thanks for your attempt you need to work hard.</b>  We will send you the result sheet to your registered Mail ID.' ;
        return render(request,'MCQTest/Result.html', {'msg': msg,'result':result})
    else:

        q = Question.objects.filter(Q(category__id = pid))
        list = [];
        for item in q:
            list.append(item.id);
        seconds = q.count() * 72000
        return render(request,'MCQTest/Practice.html', {'Que' : q, 'list': list, 'seconds':seconds})
        

'''
def home_view(request, pid= None):
    msg = ''
    if request.method == 'POST':
        questions = request.POST.get('Que');
        list = [];
        result = [];
        total = 0;
        correct_answers = 0;
        wrong_ansers = 0;
        for i in questions:
            if i.isdigit():
                list.append(i);
                total = total + 1;
        c = 0;
        correction = '';
        for item in list:
            answered = Answers.objects.get(id = item);
            choice = request.POST.get(item);
            if choice is not None:
                c = c + 1;
                if str(answered.answer.id) == str(choice):
                    correction = " Question " + item + ": <b>Correct</b>";
                    correct_answers = correct_answers + 1;
                else:
                    correction = " Question " + item + ": Worng"; + 1;
                    wrong_ansers = wrong_ansers + 1;
                result.append(correction);
        correction = " Total No. Questions : " + str(total)
        result.append(correction);
        correction = " Total No. Questions attened : " + str(c);
        result.append(correction);
        correction = " Total No. Correct Answers : " + str(correct_answers)
        result.append(correction);
        correction = " Total No. Wrong Answers : " + str(wrong_ansers);
        result.append(correction);
        per = correct_answers/total*100;
        correction = " Percentage % : " + str(round(per));
        result.append(correction);
        if per > 60:
            msg = '<b>Thanks for your successful attempt Good Luck.</b>  We will send you the result sheet to your registered Mail ID.';
        else:
            if per > 45:
                msg = '<b>Thanks for your good attempt Good Work you are near to your target.</b>  We will send you the result sheet to your registered Mail ID.';
            else:
                msg = '<b>Thanks for your attempt you need to work hard.</b>  We will send you the result sheet to your registered Mail ID.' ;
        return render(request,'MCQTest/Result.html', {'msg': msg,'result':result})
    else:
        q = Question.objects.filter(Q(category__id = pid))
        c = 0;
        list = [];
        for item in q:
            list.append(item.id);
            c = c + 1;
        seconds = c * 72000;
    return render(request,'MCQTest/home.html', {'Que' : q, 'list': list, 'seconds':seconds})
'''

def loginview(request):
    msg = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/dashboard/')
            else:
                msg = username + ' account has been disabled.'
                return render(request, 'MCQTest/Login_Page.html', {'message': msg})
        else:
            msg = 'Invalid Username and Password'
    return render(request,'MCQTest/Login_Page.html',{'message': msg})


@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def reset(request):
    return password_reset(request, template_name='MCQTest/reset.html',
        email_template_name = 'MCQTest/reset_email.html',
        subject_template_name = 'MCQTest/reset_subject.txt',
        post_reset_redirect = reverse('success'))


def reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(request, template_name='MCQTest/reset_confirm.html',
        uidb64=uidb64, token=token, post_reset_redirect=reverse('success'))

def success(request):
  return render(request, "MCQTest/success.html")
