from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render_to_response("home.html", {'hello': "Hello Josh"})