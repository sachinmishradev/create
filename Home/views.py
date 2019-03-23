from django.shortcuts import render

#  Create your views here.
from django.http import HttpResponse
import EntryByUser
def home(request):
    return HttpResponse('Hello, World!')

def home(request):
     return render(request,"home.html")
