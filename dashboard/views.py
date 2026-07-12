from django.shortcuts import render
from django.http import HttpResponse

def profile_index(request):
    return HttpResponse('your profile')
