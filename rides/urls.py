from django.urls import path

from . import views

app_name = 'rides'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('addride', views.addride, name='addride')
]
