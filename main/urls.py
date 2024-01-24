from .views import index, contact, service, blog, about
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('service/', service, name='service'),
    path('blog/', blog, name='blog'),
    path('about/', about, name='about'),
]