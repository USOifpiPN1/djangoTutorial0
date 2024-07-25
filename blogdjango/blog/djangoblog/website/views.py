from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Funcionario

# Create your views here.
def index(request):
    mFuncionarios  = Funcionario.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mFuncionarios':mFuncionarios
    }
    return HttpResponse(template.render(context, request))