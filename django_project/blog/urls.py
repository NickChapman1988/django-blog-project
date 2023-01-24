from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
    path('', views.index, name='index'),
    path('business', views.business, name='business'),
    path('register/', user_views.register, name='register'),
]
