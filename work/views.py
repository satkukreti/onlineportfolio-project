from django.shortcuts import render
from .models import Work

# Create your views here.
def home(request):
    works = Work.objects
    return render(request, 'work/home.html', {'works':works})
