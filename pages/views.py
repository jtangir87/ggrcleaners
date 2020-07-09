from django.shortcuts import render
from django.views.generic import TemplateView
from django.template.loader import get_template
from django.http import JsonResponse
from django.core.mail import send_mail
from django.contrib import messages
from django.urls import reverse

# Create your views here.
class HomeView(TemplateView):
    template_name = "pages/home.html"


def contact_us(request):
    data = dict()
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        template = get_template('contact_us.txt')
        context = {
            'name': name,
            'phone': phone,
            'email': email,
            'message': message,
        }
        content = template.render(context)
        send_mail(
            "GGRC Contact Us",
            content,
            "{}<{}>".format(name, email),
            ['jared.tangir@gmail.com'],
            # ['office@ggrcleaners.com'],
            fail_silently=False,
        )
        print("email sent")
        data["form_is_valid"] = True
    else:
        data["form_is_valid"] = False
    return JsonResponse(data)