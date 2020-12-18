from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from eprojapp import forms
from eprojapp.models import User, Tokens, Car


# Create your views here.


def paginate_qs(request, qs):
    page = request.GET.get('page', 1)
    paginator = Paginator(qs, 4)
    try:
        qs = paginator.page(page)
    except EmptyPage:
        qs = paginator.page(1)
    return qs


def home_page(request):
    return render(request, 'index.html')


def form_name_view(request):
    form = forms.UserCreateForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()
        return redirect("home")
    return render(request, 'forms.html', {'form': form})


def job_page(request):
    return render(request, 'jobs.html')


def about_page(request):
    return render(request, 'about.html')


@login_required
def users_list(request):
    users = User.objects.all()
    users = paginate_qs(request, users)
    return render(request, 'list_users.html', {'users_id': users})


@login_required
def tokens_list(request):
    tokens = Tokens.objects.all()
    tokens = paginate_qs(request, tokens)
    return render(request, 'list_tokens.html', {'users': tokens})


class CarCreateView(CreateView):
    model = Car
    fields = ('model', 'series', 'kilometer', 'price', 'img')


def sound_sensor(request):
    return render(request, 'sound_sensor.html')
