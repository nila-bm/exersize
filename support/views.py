from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('This is support page')

def index_archive(request):
    return HttpResponse('all ticket')

def index_ticket(request):
    return HttpResponse("open a ticket")