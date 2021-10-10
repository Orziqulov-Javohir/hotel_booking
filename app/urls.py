from django.urls import path
from .views import IndexPageView, AboutPageView, contact

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', contact, name='contact'),

    
]