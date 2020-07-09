
from django.urls import path
from django.views.generic import TemplateView
from .views import contact_us

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name="home"),
    path('contact-us', contact_us, name="contact_us")
]