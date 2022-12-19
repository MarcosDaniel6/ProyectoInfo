from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Denuncia
from django.template import loader
from .models import News
from .forms import NewsForm, DenunciaForm
# Create your views here.

def index(request):
    news = News.objects.filter(title__contains=request.GET.get('search',''))
    
    context = {
        'news':news
    }

    return render(request, 'blog/index.html', context)

def view(request, id):
    blog = News.objects.get(id=id)
    context = {
        'blog':blog
    }
    return render(request, 'blog/detail.html', context)

def edit(request, id):
    news = News.objects.get(id=id)
    if request.method == 'GET':        
        form = NewsForm(instance=news)
        context = {
            'form':form,
            'id':id
        }
        return render(request, 'blog/edit.html', context)
    
    if request.method == 'POST':
        form = NewsForm(request.POST, instance= news)
        if form.is_valid():
            form.save()
        
        context = {
            'form':form,
            'id':id
        }
        messages.success(request, 'Noticia Actualizada!')
        return render(request, 'blog/edit.html', context)


def create(request):    
    if request.method == 'GET':
        form = NewsForm()
        context = {
            'form':form
        }
        return render(request, 'blog/create.html', context)

    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Noticia creada!')

        return redirect(to='blog')


def delete(request, id):
    news = News.objects.get(id=id)
    if request.method == 'GET':        
        form = NewsForm(instance=news)
        context = {
            'form':form,
            'id':id
        }
        return render(request, 'blog/delete.html', context)

    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            news.delete()
        return redirect(to='blog')

def realizar_denuncia(request):
    form = DenunciaForm()
    if request.method == "GET":
        context = {
            "form": form       
        }
        return render(request, "denuncia.html", context)

    if request.method == "POST":
        form = DenunciaForm(request.POST)
        

        if form.is_valid():
            
            # denuncia.direccion = form.cleaned_data['direccion']
            # denuncia.texto_denuncia = form.cleaned_data['texto_denuncia']
            # denuncia.email = form.cleaned_data['email']
            # denuncia.telefono = form.cleaned_data['telefono']


            form.save()
            
    return render(request, 'denuncia.html', {'form' : form})

def denunciaformal(request):
    return render(request, 'denunciaformal.html', {})