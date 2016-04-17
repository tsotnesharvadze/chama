from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get/$', views.get_recipes, name='get_recipes'),
    url(r'^ingredients/$', views.get_ingredients, name="get_ingredients")
]
