from django.shortcuts import render

# Create your views here.
from django.views import View


class home_page(View):
    def get(self, request):
        return render(request, 'home_page.html')



def site_header_component(request):
    return render(request, 'shared/header_partial.html')


def site_footer_component(request):
    return render(request, 'shared/footer_partial.html')