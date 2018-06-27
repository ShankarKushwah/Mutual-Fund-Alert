from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
# from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, HttpResponse
from .forms import UserForm
from .models import Register_as_Guest, Register_Full
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View


def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    return render(request, 'home/contact.html')


def r1(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'home/1.html')
    context = {
        "form": form,
    }
    return render(request, 'home/register.html', context)


def register(request):
    return render(request, 'home/register.html')


def login(request):
    return render(request, 'home/login.html')
