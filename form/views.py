from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from form.models import Academic
from .forms import AcademicForm 


def main(request):
    form = AcademicForm
    if request.method == 'POST':
        form_data = AcademicForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('شكرا يا مساح')
        else:
            return HttpResponse('invalid data')
    context = {
        "form": form
    }
    return render(request, 'main.html', context)



def login_page(request):
    user = User.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username= username, password= password)
        if user is not None:
            login(request, user)
            return redirect('filter_data')
        else:
            return HttpResponse('Error404')
    context = {}
    return render(request, 'login.html', context)


def logout_page(request):
    logout(request)
    return redirect('main')


@login_required(login_url='main')
def filter_data(request):
    all_data = Academic.objects.all().count()
    context = {
        "all_data": all_data
    }
    return render(request, 'filter.html', context)


@login_required(login_url='main')
def show_data(request, pk):
    data = Academic.objects.filter(batch=pk)
    count_data = data.count()
    context = {
        "data": data,
        "count_data": count_data,
        "pk": pk,
    }
    return render(request, 'data.html', context)