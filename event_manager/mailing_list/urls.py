from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),  # Form to subscribe to the mailing list
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),  # Form to unsubscribe from the mailing list
]