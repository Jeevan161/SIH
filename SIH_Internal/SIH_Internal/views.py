from django.http import JsonResponse
from django.shortcuts import render



def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')
def caseRegister(request):
    return render(request, 'RegisterCase.html')
