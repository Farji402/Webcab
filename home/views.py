from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from signup.models import Janta
from django.views.decorators.csrf import csrf_protect



def profile(request):
    if request.session.has_key('outlook_id'):
        dbuser = Janta.objects.get(outlook_id = request.session['outlook_id'])
        return render(request, 'home/profile page.html', {'username': request.session['username'],
                                                          'dbuser': dbuser})
    else:
        return render(request, 'home/home_page.html')

@csrf_protect
def upload_dp(request):
    if request.session.has_key('outlook_id'):
        if request.method == 'POST':
            form = form_dp(request.POST, request.FILES)
            if form.is_valid():
                dbuser = Janta.objects.get(outlook_id = request.session['outlook_id'])
                dbuser.dp = form.cleaned_data['dp']
                dbuser.save()
                return render(request, 'home/profile page.html',
                              {'username': request.session['username'],
                               'profile_photo': dbuser.dp})
            else:
                dbuser = Janta.objects.get(outlook_id=request.session['outlook_id'])
                return render(request, 'home/profile page.html', {'response': "Try again!",
                                                                  'username': request.session['username'],
                                                                  'profile_photo': dbuser.dp})
        else:
            return render(request, 'home/fun.html')

    else:
        return render(request, 'home/home_page.html')

def booking(request):
    if request.session.has_key('outlook_id'):
        return render(request, 'home/booking page.html')
    else:
        return render(request, 'home/home_page.html')

def about(request):
    if request.session.has_key('outlook_id'):
        return render(request, 'home/booking page.html')
    else:
        return render(request, 'home/about_page.html')

def help(request):
    if request.session.has_key('outlook_id'):
        return render(request, 'home/booking page.html')
    else:
        return render(request, 'home/Help_page.html')

def setting(request):
    if request.session.has_key('outlook_id'):
        return render(request, 'home/setting page.html', {'username': request.session['username'],
                                                          'mobile': request.session['phone']})
    else:
        return render(request, 'home/home_page.html')

@csrf_protect
def edit_general(request):
    if request.session.has_key('outlook_id'):
        if request.method == 'POST':
            form_edit = form_edit_general(request.POST)
            if form_edit.is_valid():
                dbuser = Janta.objects.get(outlook_id = request.session['outlook_id'])
                dbuser.user_name = request.POST['username']
                dbuser.mob = request.POST['phone']
                dbuser.save()
                return render(request, 'home/setting page.html', {'form_response': "Login again to see the changes.",
                                                                  'username': request.session['username'],
                                                                  'mobile': request.session['phone']})
            else:
                return render(request, 'home/setting page.html', {'form_response': "You messed up in one of the fields! Try again",
                                                                  'username': request.session['username'],
                                                                  'mobile': request.session['phone']})

        else:
            return render(request, 'home/fun.html')

    else:
        return render(request, 'home/home_page.html')

@csrf_protect
def edit_security(request):
    if request.session.has_key('outlook_id'):
        if request.method == 'POST':
            form_edit = form_edit_security(request.POST)
            if form_edit.is_valid():
                dbuser = Janta.objects.get(outlook_id = request.session['outlook_id'])
                if dbuser.password == request.POST['current_password']:
                    dbuser.password = request.POST['password']
                    dbuser.save()
                    return render(request, 'home/setting page.html', {'form_response': "Login again to see the changes.",
                                                                      'username': request.session['username'],
                                                                      'mobile': request.session['phone']})
                else:
                    return render(request, 'home/setting page.html', {'form_response': "Current password entered is wrong! Try again.",
                                                                      'username': request.session['username'],
                                                                      'mobile': request.session['phone']})
            else:
                return render(request, 'home/setting page.html', {'form_response': "You didn't fill the required fields correctly! Try again",
                                                                  'username': request.session['username'],
                                                                  'mobile': request.session['phone']})
        else:
            return render(request, 'home/fun.html')
    else:
        return render(request, 'home/home_page.html')


def logout(request):
    try:
        del request.session['outlook_id']
    except:
        pass
    return render(request, 'home/home_page.html')


@csrf_protect
def login(request):
    my_response = 'Invalid details! please try again.'

    if request.method == 'POST':
        login_data = login_form(request.POST)

        if login_data.is_valid():
            outlook_id = request.POST['outlook_id']
            dbuser = Janta.objects.get(outlook_id = outlook_id)
            request.session['outlook_id'] = outlook_id
            request.session['username'] = dbuser.user_name
            request.session['phone'] = dbuser.mob
            request.session.set_expiry(7200)

        else:
            return render(request, 'home/home_page.html', {'response': my_response})
    else:
        return render(request, 'home/fun.html')


    return render(request, 'home/booking page.html')


def index(request):
    if request.session.has_key('outlook_id'):
        return render(request, 'home/booking page.html')
    else:
        return render(request, 'home/home_page.html')
