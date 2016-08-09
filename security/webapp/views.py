# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django.utils import timezone
from .models import Devices
from .models import EditLog 
from .forms import LogForm
from .forms import DevicesForm
from .forms import JoinForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
import json


def post_list(request):
    return render(request, 'webapp/post_list.html')

def history_page(request):
    history_list=EditLog.objects.order_by('update_date')[:]
    return render(request, 'webapp/history_page.html',{'history_list':history_list})

def main_page(request):
    deviceList=Devices.objects.order_by('-name')[:]
    return render(request, 'webapp/main_page.html', {'deviceList':deviceList})

def user_info(request):
    return render(request, 'webapp/user_info.html')

def RegisterDevice(request):
    if request.method == "POST":
        form = DevicesForm(request.POST)
        if form.is_valid():
            device = form.save(commit=False)
            device.author = request.user
            device.save()
            return HttpResponseRedirect('/main/page')
           # return HttpResponseRedirect(reverse('main_page'))
    else:
        form = DevicesForm()
    return HttpResponseRedirect('/')

def loginView(request):
  return render(request, 'webapp/main_page.html')

def loginAction(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('webapp.views.main_page')
        else:
            return HttpResponse("Failed :Bad username")
    else:
       # return HttpResponse("Failed: Bad password")
        return HttpResponseRedirect(reverse('post_list'))

def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('post_list'))

def device_edit(request, pk):
    device = get_object_or_404(Devices, pk=pk)
    form = DevicesForm(request.POST or None , instance =device)
    if request.method == "POST":
        if form.is_valid():
            his= EditLog(writer=request.user, serial=request.POST['serial_num'] )
            his.save()
            if device.serial_num!= request.POST['serial_num']:
                device.serial_num = request.POST['serial_num'];
            if device.ip_addr != request.POST['ip_addr']:
                device.ip_addr=request.POST['ip_addr']
            if device.name != request.POST['name']:
                device.name = request.POST['name']
            if 'enable' in form.cleaned_data:
                device.enable = request.POST['enable']
        device.author = request.user
        device.save()
    return HttpResponseRedirect(reverse('main_page'))

def delete_device(request, pk):
    instance = Devices.objects.get(pk=pk)
    instance.delete()
    return HttpResponseRedirect(reverse('main_page'))

def join_user(request):
    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1']
            )
            return HttpResponseRedirect('/')
    else:
        form=JoinForm()
    datas = RequestContext(request, {
        'form': form
    })
    return HttpResponseRedirect('/')

def change_user(request, pk):
    if request.method =='POST':
        us = User.objects.get(pk=pk)
        us.set_password(request.POST['password1'])
        us.save()
    else:
        us = User.objects.get(pk=pk)
        us.set_password(request.password1)
        us.save()

    username = request.POST['username']
    password = request.POST['password1']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('user_info'))
        else:
            return HttpResponse("Disable tp access account.")
    else:
        return HttpResponse("Invalid this  account.")

    return HttpResponseRedirect(reverse('user_info'))

# Create your views here.
