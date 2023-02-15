from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from .models import contact_us_model

class contact_page(View):
    def get(self, request):
        return render(request, 'contact_page.html')

    def post(self, request):

        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        text = request.POST.get('comments')

        new_contact_msg = contact_us_model(name=name, email=email, subject=subject,
                                               phone=phone, text=text)
        new_contact_msg.save()
        return redirect('contact-page')

