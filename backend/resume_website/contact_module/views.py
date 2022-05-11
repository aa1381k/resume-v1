from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from .forms import contact_us_form
from .models import contact_us_model
from user_resume_data.models import basic_info_model


class contact_page(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            form = contact_us_form(initial={'email':user.email})
            context = {
                'user':request.user,
                'form':form,
            }
            return render(request, 'contact_page.html', context)

        else:
            return render(request, 'contact_page.html')

    def post(self, request):
        form = contact_us_form(request.POST)
        if form.is_valid():

            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            phone = form.cleaned_data.get('phone')
            text = form.cleaned_data.get('text')

            new_contact_msg = contact_us_model(name=name, email=email, subject=subject,
                                                   phone=phone, text=text)
            new_contact_msg.save()
        return redirect('contact-page')

