from datetime import datetime
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import GasServiceRequest
from .forms import GasServiceRequestForm

# Create your views here.

def home(request):
    return render(request, 'gas_request/home.html')


class UserSignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'gas_request/signup.html'         # Update with your template path
    success_url = reverse_lazy('login')               # Redirect to login page after successful signup


class CustomLoginView(LoginView):
    template_name = 'gas_request/login.html'       # Update with your template path
    success_url = reverse_lazy('home')             # Redirect to the home page after successful login



def custom_logout(request):
    logout(request)
    return redirect('home')          # Redirect to the home page after successful logout

@login_required
def Create_request(request):
    if request.method == 'POST':
        form = GasServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = GasServiceRequestForm()
    return render(request, 'gas_request/service_request.html', {'form': form})


@login_required
def track_request(request):
    print(request.user)
    requests = GasServiceRequest.objects.filter(user = request.user).order_by('timestamp')
    return render(request, 'gas_request/track_request.html', {'requests':requests})


@login_required
def mark_completed(request):
    if request.user.is_staff:
        requests = GasServiceRequest.objects.all().order_by('timestamp')
        return render(request, 'gas_request/mark_completed.html', {'requests':requests})
    else:
        return HttpResponse("You Are Not Authorise To Do This Operation !!")


def update_request(request, id):
    t = GasServiceRequest.objects.get(pk=id)
    if not t.is_completed:
        t.is_completed = True
        t.completion_timestamp = datetime.now()
        t.save()
        return redirect ('home')
    return redirect('home')