from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .form import RegistrationForm, CompanyFilterForm
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView
from .serializers import CompanySerializer
from django.views import View
import json


# Create your views here.
def index(request):
    JOpening = job_opening.objects.all()
    paginator = Paginator(JOpening, 9)
    page = request.GET.get('page')
    try:
        data_page = paginator.page(page)
    except PageNotAnInteger:
        data_page = paginator.page(1)
    except EmptyPage:
        data_page = paginator.page(paginator.num_pages)

    context = {
        'data_page': data_page,
        }
    return render(request, "JobBoard/index.html", context)


class opening_details(DetailView):
    model = job_opening
    template_name = 'JobBoard/details.html'
    context_object_name = 'object' 


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'JobBoard/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = RegistrationForm()
    return render(request, 'JobBoard/register.html', {'form': form})



@login_required
def home_view(request):
    JOpening = job_opening.objects.all()
    paginator = Paginator(JOpening, 9)
    page = request.GET.get('page')
    try:
        data_page = paginator.page(page)
    except PageNotAnInteger:
        data_page = paginator.page(1)
    except EmptyPage:
        data_page = paginator.page(paginator.num_pages)

    context = {
        'data_page': data_page,
        }
    return render(request, "JobBoard/home.html", context)




def companies_page(request):
    Companies = Company.objects.all().order_by('name')
    queryset = Company.objects.all()
    form = CompanyFilterForm(request.GET)
    if form.is_valid():
        sector = form.cleaned_data.get('sector')
        if sector:
            queryset = queryset.filter(sector=sector)
    paginator = Paginator(Companies, 9)
    page = request.GET.get('page')
    try:
        data_page = paginator.page(page)
    except PageNotAnInteger:
        data_page = paginator.page(1)
    except EmptyPage:
        data_page = paginator.page(paginator.num_pages)

    context = {
        'data_page': data_page,
        'queryset': queryset,
        'form': form,
        }
    return render(request, "JobBoard/companies.html", context)


def companies_search_page(request):
    queryset = Company.objects.all()
    form = CompanyFilterForm(request.GET)
    if form.is_valid():
        sector = form.cleaned_data.get('sector')
        if sector:
            queryset = queryset.filter(sector=sector)
    
    context = {
        'queryset': queryset,
        'form': form,
        }
    return render(request, "JobBoard/companies_search.html", context)



class CompanyJsonView(View):
    template_name = "JobBoard/charts.html"

    def get(self, request, *args, **kwargs):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        #data = serializer.data
        company_count = {}
        for companies in serializer.data:
            company = companies["sector"]
            company_count[company] = company_count.get(company, 0) + 1

        sector_data = json.dumps(company_count)

        employee_size_count = {}
        for employee_sizes in serializer.data:
            employee_size = employee_sizes["employee_size"]
            employee_size_count[employee_size] = employee_size_count.get(employee_size, 0) + 1

        employee_size_data = json.dumps(employee_size_count)

        return render(request, self.template_name, {'sector_data': sector_data, "employee_data": employee_size_data})


def contact(request):
    return render(request, "JobBoard/contact.html")


def about_page(request):
    return render(request, "JobBoard/about.html")
