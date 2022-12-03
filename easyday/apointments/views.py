from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DeleteView
from .forms import ClientForm
from .forms import ServiceForm
from apointments.forms import AppointmentForm
from apointments.models import Employee, Appointment, Client
from django.http import HttpResponseRedirect


def homepage_view(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        name = request.POST['name']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = Employee.objects.create_user(username, email, pass1)
        myuser.first_name = name
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your Account has been successfully created")

        return redirect("signin")

    return render(request, "signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            name = user.first_name

            messages.success(request, "Logged In Successfully!")
            return render(request, 'home.html', {'name': name})
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('homepage')

    return render(request, "signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('homepage')


class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    success_url = reverse_lazy('list_appointment')
    template_name = 'create_appointment.html'


class AppoiuntmentListView(ListView):
    model = Appointment
    context_object_name = 'appointments'
    template_name = 'list_appointment.html'


class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'delete_appointment.html'
    success_url = reverse_lazy('list_appointment')


def AddClient(request):
    submitted = False
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You Have Added a New Client!")
            return redirect('add_client')
    else:
        form = ClientForm
        if 'submitted' in request.GET:
            submitted = True
    form = ClientForm
    return render(request, 'add_client.html', {'form': form, 'submitted': submitted})


def AddService(request):
    submitted = False
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You Have Added a New Service!")
            return redirect('add_service')
    else:
        form = ServiceForm
        if 'submitted' in request.GET:
            submitted = True
    form = ServiceForm
    return render(request, 'add_service.html', {'form': form, 'submitted': submitted})


