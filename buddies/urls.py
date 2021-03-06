from django.urls import path

from . import views

app_name = 'buddies'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('addbuddy', views.addbuddy, name='addbuddy'),
    path('feedback', views.feedback, name='feedback')
]
