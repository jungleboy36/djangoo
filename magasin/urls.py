from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name='index'),
path('del_art/<int:id>',views.del_art,name='del_art'),
path('/categorie',views.categorie,name='categorie'),
path('del_cat/<int:id>',views.del_cat,name='del_cat'),
]