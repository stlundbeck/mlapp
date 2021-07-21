from django.urls import path

from . import views

from dataStaging.views import upload_views

app_name = 'home'
urlpatterns = [
    path('', views.MainView.as_view(), name='home'),
    path('upload/', upload_views, name='upload')
]
