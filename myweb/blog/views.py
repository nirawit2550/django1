from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def blog (request):
    return HttpResponse("นิรวิทธ์ พวงนาค.2")