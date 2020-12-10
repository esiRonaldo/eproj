from django.core.paginator import Paginator, EmptyPage
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


def pagination(request):
    token_list = Tokens.objects.all()
    paginator = Paginator(token_list, 4)  # Show  tokens per page.
    number_of_pages = paginator.num_pages

    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except EmptyPage:
        page_obj = paginator.get_page(1)
    page_obj= {'page_obj': page_obj}
    return page_obj


def tokens_list(request):
    tokens = Tokens.objects.all()
    dict = {'user_ids': tokens}

   # pagination(request)
    return render(request, 'list_tokens.html', context=dict)
