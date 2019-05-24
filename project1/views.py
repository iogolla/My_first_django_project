from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
import datetime

# Create your views here.



def index(date):
    now = datetime.datetime.now()
    return render(date, 'index.html', {'todays_date': now})
