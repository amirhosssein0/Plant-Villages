from django.urls import path
from .views import *


app_name = 'pages'
urlpatterns = [
    path('contact-us/', ContactUsPageView.as_view(), name='contact-us'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]
