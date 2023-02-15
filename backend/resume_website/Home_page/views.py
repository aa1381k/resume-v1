from django.shortcuts import render
from .models import Slider, home_page_settings, about_us_model
from user_resume_data.models import basic_info_model
from blog_module.models import blog_model
# Create your views here.
from django.views import View
from site_module.models import SiteSetting, SliderModel, FooterLinkBox, FooterLink
from account_module.models import User_model

class home_page(View):
    def get(self, request):
        sliders = Slider.objects.filter(is_active=True)
        home_settings = home_page_settings.objects.filter(is_active=True).first()
        blogs = blog_model.objects.filter(is_active=True).order_by('create_date')[:3]
        context = {
            'slider_images' : sliders,
            'home_settings' : home_settings,
            'blogs' : blogs,
            'user' : request.user,
        }
        return render(request, 'home_page.html', context)

class about_page(View):
    def get(self, request):

        about_settings = about_us_model.objects.filter(is_active=True).first()

        context = {
            'about_settings' : about_settings,
        }

        return render(request, 'about_page.html', context)

def site_header_component(request):

    if request.user.is_authenticated:

        user = request.user
        user_info = User_model.objects.filter(email__iexact=user.email).first()
        if user_info != None:

            avatar = user_info.avatar

            context = {
                'user_avatar' : avatar
            }
        else:
            context = {}

        return render(request, 'shared/header_partial.html', context)

    return render(request, 'shared/header_partial.html')


def site_footer_component(request):
    context = {
        'footer_link_boxes' : FooterLinkBox.objects.all(),
        'footer_links' : FooterLink.objects.all(),
    }

    return render(request, 'shared/footer_partial.html', context)