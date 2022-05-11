from django.shortcuts import render
from .models import Slider, home_page_settings, about_us_model
from user_resume_data.models import basic_info_model
# Create your views here.
from django.views import View


class home_page(View):
    def get(self, request):
        sliders = Slider.objects.filter(is_active=True)
        home_settings = home_page_settings.objects.filter(is_active=True).first()
        context = {
            'slider_images' : sliders,
            'home_settings' : home_settings,
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
        user_info = basic_info_model.objects.filter(user_base_info_id=user.id).first()
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
    return render(request, 'shared/footer_partial.html')