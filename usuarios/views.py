from django.shortcuts import render,HttpResponse

# Create your views here.


def cadastro(request):
    return HttpResponse("Página de cadastro de usuários")

def login(request):
    return HttpResponse('login')