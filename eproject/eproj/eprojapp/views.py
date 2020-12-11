from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, redirect

from eprojapp import forms
from eprojapp.models import User, Tokens


# Create your views here.


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


def tokens_list(request):
    tokens = Tokens.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(tokens, 4)
    try:
        users = paginator.page(page)
        print("paaaaaaaaaaaasssssssssssss")
    except EmptyPage:
        users = paginator.page(1)
        print("erooooooooooooooooooor")

    return render(request, 'list_tokens.html', {'users': users})
