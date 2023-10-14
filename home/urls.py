from django.urls import path
from .views import home, about, testemonial, service, contact, portfolio

urlpatterns = [
    path('', home),
    path('about/', about),
    path('portfolio/', portfolio),
    path('service/', service),
    path('contact/', contact),
    path('testemonial/', testemonial),
]

