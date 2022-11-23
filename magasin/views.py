from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse
from magasin.models import Article,Categorie

def index(request):
    art = Article.objects.all().values()
    template = loader.get_template('home.html')
    context = {
    'art': art,
 }
    return HttpResponse(template.render(context, request))

def del_art(request, id):
 article = Article.objects.get(id=id)
 article.delete()
 return HttpResponseRedirect(reverse('index'))

def del_cat(request, id):
 categorie = Categorie.objects.get(id=id)
 categorie.delete()
 return HttpResponseRedirect(reverse('categorie'))
def categorie (request): 
      cat = Categorie.objects.all().values()
      template =loader.get_template('categorie.html')
      context = { 'cat' : cat,}
      return HttpResponse (template.render(context,request))